#!/usr/bin/env python3
"""
刷新 live_status.json - 从 tasks_source.json 生成实时状态数据
"""
import json, pathlib
from datetime import datetime

BASE = pathlib.Path(__file__).parent.parent
DATA = BASE / 'data'
TASKS_FILE = DATA / 'tasks_source.json'
OUTPUT_FILE = DATA / 'live_status.json'

def main():
    # 读取任务数据
    tasks = []
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
    except Exception:
        tasks = []

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
    output = {
        'tasks': tasks,
        'agents': [],
        'stats': stats,
        'syncStatus': {
            'ok': True,
            'message': '正常',
            'lastSync': datetime.utcnow().isoformat() + 'Z'
        },
        'lastUpdate': datetime.utcnow().isoformat() + 'Z'
    }

    # 写入文件
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✅ Refreshed live_status.json: {len(tasks)} tasks")

if __name__ == '__main__':
    main()
