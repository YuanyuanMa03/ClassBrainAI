#!/usr/bin/env python3
"""
一次性迁移 tasks_source.json 到统一班级状态机。

支持:
- --dry-run: 只生成迁移报告，不写文件（默认）
- --apply: 执行迁移写入，并先创建备份
"""

import argparse
import collections
import datetime as dt
import json
import pathlib
import shutil
import sys
from typing import Dict, Tuple


VALID_STATES = {
    "Pending", "Monitor", "Study", "Chair", "Assigned",
    "Doing", "Review", "Done", "Blocked", "Cancelled",
}

# 仅用于一次性历史迁移，不在运行态使用
LEGACY_TO_CANONICAL = {
    "Inbox": "Pending",
    "Taizi": "Monitor",
    "Zhongshu": "Study",
    "Menxia": "Chair",
    "Next": "Assigned",
    "Technical": "Doing",
    "Organization": "Doing",
}

STATE_ORG_DEFAULT = {
    "Pending": "班主任",
    "Monitor": "班长",
    "Study": "学习委员",
    "Chair": "班委主席",
    "Assigned": "副班长",
    "Doing": "各班委",
    "Review": "副班长",
    "Done": "完成",
    "Blocked": "阻塞",
    "Cancelled": "取消",
}

ORG_PLACEHOLDERS = {"", "-", "执行中", "阻塞", "完成", "待执行", "收件", "待处理"}


def canonicalize_state(raw_state) -> Tuple[str, str]:
    if not isinstance(raw_state, str):
        return "Pending", "invalid_non_string"
    s = raw_state.strip()
    if not s:
        return "Pending", "invalid_empty"
    if s in VALID_STATES:
        return s, "valid"
    if s in LEGACY_TO_CANONICAL:
        return LEGACY_TO_CANONICAL[s], "legacy"
    return "Pending", "invalid_unknown"


def normalize_task(task: Dict) -> Tuple[Dict, Dict]:
    detail = {"changed": False, "changes": []}

    old_state = task.get("state")
    new_state, reason = canonicalize_state(old_state)
    if old_state != new_state:
        task["state"] = new_state
        detail["changed"] = True
        detail["changes"].append(
            {"field": "state", "from": old_state, "to": new_state, "reason": reason}
        )

    old_prev = task.get("_prev_state")
    if old_prev is not None:
        new_prev, prev_reason = canonicalize_state(old_prev)
        if old_prev != new_prev:
            task["_prev_state"] = new_prev
            detail["changed"] = True
            detail["changes"].append(
                {"field": "_prev_state", "from": old_prev, "to": new_prev, "reason": prev_reason}
            )

    sched = task.get("_scheduler")
    if isinstance(sched, dict):
        snap = sched.get("snapshot")
        if isinstance(snap, dict):
            old_snap = snap.get("state")
            new_snap, snap_reason = canonicalize_state(old_snap)
            if old_snap != new_snap:
                snap["state"] = new_snap
                detail["changed"] = True
                detail["changes"].append(
                    {"field": "_scheduler.snapshot.state", "from": old_snap, "to": new_snap, "reason": snap_reason}
                )

    org = task.get("org")
    if new_state in STATE_ORG_DEFAULT and (not isinstance(org, str) or org.strip() in ORG_PLACEHOLDERS):
        target_org = STATE_ORG_DEFAULT[new_state]
        if org != target_org:
            task["org"] = target_org
            detail["changed"] = True
            detail["changes"].append(
                {"field": "org", "from": org, "to": target_org, "reason": "state_default_org"}
            )

    return task, detail


def main() -> int:
    parser = argparse.ArgumentParser(description="迁移 tasks_source.json 到统一状态机")
    parser.add_argument("--file", default="data/tasks_source.json", help="任务文件路径")
    parser.add_argument("--report-dir", default="data/migration_reports", help="报告输出目录")
    parser.add_argument("--backup-dir", default="data/backups", help="备份目录（仅 --apply 时使用）")
    parser.add_argument("--apply", action="store_true", help="执行写入；默认 dry-run")
    args = parser.parse_args()

    task_file = pathlib.Path(args.file).resolve()
    report_dir = pathlib.Path(args.report_dir).resolve()
    backup_dir = pathlib.Path(args.backup_dir).resolve()
    report_dir.mkdir(parents=True, exist_ok=True)

    if not task_file.exists():
        print(f"[migrate] 任务文件不存在: {task_file}", file=sys.stderr)
        return 1

    try:
        raw = json.loads(task_file.read_text(encoding="utf-8") or "[]")
        if not isinstance(raw, list):
            print("[migrate] tasks_source.json 不是数组，已中止", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"[migrate] 读取失败: {e}", file=sys.stderr)
        return 1

    migrated = []
    details = []
    state_before = collections.Counter()
    state_after = collections.Counter()
    change_kind_counter = collections.Counter()

    for idx, item in enumerate(raw):
        if not isinstance(item, dict):
            details.append({"index": idx, "id": None, "changed": False, "skipped": "non_dict"})
            continue
        state_before[str(item.get("state"))] += 1
        task, detail = normalize_task(dict(item))
        state_after[str(task.get("state"))] += 1
        task_id = task.get("id")
        if detail["changed"]:
            for c in detail["changes"]:
                change_kind_counter[c["field"]] += 1
            details.append({"index": idx, "id": task_id, **detail})
        migrated.append(task)

    changed_count = sum(1 for d in details if d.get("changed"))
    now = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = report_dir / f"task_state_migration_{now}.json"

    report = {
        "ok": True,
        "mode": "apply" if args.apply else "dry-run",
        "file": str(task_file),
        "totalTasks": len(migrated),
        "changedTasks": changed_count,
        "stateBefore": dict(state_before),
        "stateAfter": dict(state_after),
        "changeKinds": dict(change_kind_counter),
        "changedSamples": details[:50],
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    backup_path = None
    if args.apply:
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / f"tasks_source_{now}.json.bak"
        shutil.copy2(task_file, backup_path)
        task_file.write_text(json.dumps(migrated, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[migrate] mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"[migrate] tasks: {len(migrated)}, changed: {changed_count}")
    print(f"[migrate] report: {report_path}")
    if backup_path:
        print(f"[migrate] backup: {backup_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
