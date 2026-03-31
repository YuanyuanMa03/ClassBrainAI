#!/usr/bin/env python3
"""
刷新 live_status.json - 从 tasks_source.json 生成实时状态数据
"""
import json, pathlib
from datetime import datetime, timezone

BASE = pathlib.Path(__file__).parent.parent
DATA = BASE / 'data'
TASKS_FILE = DATA / 'tasks_source.json'
OUTPUT_FILE = DATA / 'live_status.json'

VALID_STATES = {
    'Pending', 'Monitor', 'Study', 'Chair', 'Assigned',
    'Doing', 'Review', 'Done', 'Blocked', 'Cancelled',
}


def normalize_state(state):
    if not isinstance(state, str):
        return 'Pending'
    s = state.strip()
    if not s:
        return 'Pending'
    if s in VALID_STATES:
        return s
    return 'Pending'

def main():
    # 读取任务数据
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
    except Exception:
        tasks = []

    normalised = []
    for t in tasks:
        if not isinstance(t, dict):
            continue
        nt = dict(t)
        nt['state'] = normalize_state(nt.get('state', 'Pending'))
        normalised.append(nt)
    tasks = normalised

    # 统计数据
    stats = {
        'total': len(tasks),
        'byState': {},
        'byOrg': {}
    }

    for task in tasks:
        state = task.get('state', 'Unknown')
        org = task.get('org', 'Unknown')
        stats['byState'][state] = stats['byState'].get(state, 0) + 1
        stats['byOrg'][org] = stats['byOrg'].get(org, 0) + 1

    # 构建输出数据
    now_utc = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    output = {
        'tasks': tasks,
        'agents': [],
        'stats': stats,
        'syncStatus': {
            'ok': True,
            'message': '正常',
            'lastSync': now_utc
        },
        'lastUpdate': now_utc
    }

    # 写入文件
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ Refreshed live_status.json: {len(tasks)} tasks")

if __name__ == '__main__':
    main()
