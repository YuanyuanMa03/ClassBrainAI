# ClassBrainAI 设计方案

> 将 edict 班级Agent体系制多 Agent 系统改造为班级主题
>
> 设计日期：2026-03-22

---

## 概述

ClassBrainAI 是基于 edict 架构的多 Agent 协作系统，采用"班级"作为主题隐喻。保留完整的工作流（分拣→规划→审议→派发→执行）和核心功能，替换术语和视觉风格为校园风格。

---

## 1. Agent 角色映射

| edict | ClassBrainAI | 目录名 | 职责 |
|-------|--------------|--------|------|
| 太子 | 班长 | monitor | 消息分拣、初步判断、任务创建 |
| 学习委员组 | 学习委员 | study | 方案规划、分解任务 |
| 班委主席组 | 班委主席 | chair | 方案审议、质量把关 |
| 副班长组 | 副班长 | vice_monitor | 任务派发、协调执行 |
| 技术委员组 | 技术委员 | technical | 代码、技术任务 |
| 后勤委员组 | 后勤委员 | logistics | 基础设施、脚本工具 |
| 生活委员组 | 财务委员 | finance | 数据统计、资源管理 |
| 文艺委员组 | 文艺委员 | arts | 文档、知识库 |
| 纪律委员组 | 纪律委员 | discipline | 规范、质量检查 |
| 吏部 | 组织委员 | organization | 任务分配、配置 |
| 早朝 | 早读委员 | morning_reading | 每日资料收集 |

### 状态流程

```
待处理(Pending) → 班长(Monitor) → 学习委员(Study) → 班委主席(Chair) → 已派发(Assigned) → 执行中(Doing) → 待审查(Review) → ✅已完成(Done)
                                      ↑                           │
                                      └────── 驳回 ────────────────┘
```

---

## 2. 术语对照表

### 角色术语

| 类别 | edict | ClassBrainAI |
|------|-------|--------------|
| 用户 | 班主任 | 班主任 |
| 分拣官 | 太子 | 班长 |
| 规划官 | 学习委员组 | 学习委员 |
| 审议官 | 班委主席组 | 班委主席 |
| 派发官 | 副班长组 | 副班长 |
| 执行官 | 六部 | 各班委 |

### 任务术语

| 类别 | edict | ClassBrainAI |
|------|-------|--------------|
| 任务 | 任务 | 任务 |
| 任务ID | JJC-YYYYMMDD-NNN | CB-YYYYMMDD-NNN |
| 创建任务 | 传旨 | 发布任务 |
| 完成任务 | 回奏 | 汇报完成 |
| 驳回 | 驳回 | 驳回 |
| 批准 | 批准 | 批准 |

### 状态名称

| edict | ClassBrainAI | 说明 |
|-------|--------------|------|
| Pending | Pending | 待处理 |
| Taizi | Monitor | 班长处理中 |
| Zhongshu | Study | 学习委员处理中 |
| Menxia | Chair | 班委主席审议中 |
| Assigned | Assigned | 已派发 |
| Doing | Doing | 执行中 |
| Review | Review | 待审查 |
| Done | Done | 已完成 |
| Cancelled | Cancelled | 已取消 |
| Blocked | Blocked | 已暂停 |

---

## 3. UI 视觉设计

### 色彩方案（校园风格）

```
主色调：青色/蓝色系
- 主色：#0EA5E9 (天空蓝)
- 辅色：#10B981 (青绿色)
- 背景：#F8FAFC (浅灰白)
- 文字：#1E293B (深蓝灰)
- 强调：#F59E0B (琥珀黄，用于重点)

替换 edict 的：
- 红色 #DC2620 → 蓝色 #0EA5E9
- 金色 #FBBF24 → 青绿 #10B981
```

### UI 元素替换

| edict | ClassBrainAI |
|-------|--------------|
| 龙纹图标 | 书本/学士帽图标 |
| 玉玺印章 | 校徽印章 |
| 卷轴背景 | 黑板/笔记本背景 |
| 朱砂红印章 | 蓝绿色印章 |
| 古典边框 | 简约线条边框 |

### 看板布局（保持 10 面板）

1. 任务概览
2. 班级动态
3. 班级成员
4. 待处理任务
5. 班长工作台
6. 学习委员工作台
7. 班委主席工作台
8. 副班长工作台
9. 执行中任务
10. 已完成任务

---

## 4. 项目结构

```
ClassBrainAI/
├── agents/                    # Agent 人格定义
│   ├── monitor/SOUL.md        # 班长
│   ├── study/SOUL.md          # 学习委员
│   ├── chair/SOUL.md          # 班委主席
│   ├── vice_monitor/SOUL.md   # 副班长
│   ├── technical/SOUL.md      # 技术委员
│   ├── logistics/SOUL.md      # 后勤委员
│   ├── finance/SOUL.md        # 财务委员
│   ├── arts/SOUL.md           # 文艺委员
│   ├── discipline/SOUL.md     # 纪律委员
│   ├── organization/SOUL.md   # 组织委员
│   └── morning_reading/SOUL.md # 早读委员
├── scripts/                   # 工具脚本
│   ├── class_board.py         # 看板命令（移植 edict）
│   ├── file_lock.py           # 文件锁（直接复用）
│   └── utils.py               # 工具函数（直接复用）
├── data/                      # 数据存储
│   ├── tasks_source.json      # 任务源数据
│   └── live_status.json       # 实时状态（生成）
├── dashboard/                 # 看板前端
│   ├── server.py              # API 服务器
│   ├── dashboard.html         # 单文件看板
│   └── dist/                  # React 构建产物（可选）
├── docs/                      # 文档
├── tests/                     # 测试
├── config/                    # 配置
└── README.md
```

---

## 5. 开发计划

### Phase 1: Agent 人格设计

**任务：** 从 edict 复制 11 个 SOUL.md，全文替换术语，保持逻辑不变

**输入：** `edict/agents/*/SOUL.md`
**输出：** `ClassBrainAI/agents/*/SOUL.md`

**替换规则：**
- 所有角色名称按术语表替换
- 所有状态名称按术语表替换
- 保持核心流程和约束不变
- 保持语气风格适配角色

### Phase 2: 看板 CLI 工具

**任务：** 移植 `kanban_update.py` → `class_board.py`

**输入：** `edict/scripts/kanban_update.py`
**输出：** `ClassBrainAI/scripts/class_board.py`

**修改要点：**
- 替换状态常量 `STATES`
- 替换状态转换规则 `_VALID_TRANSITIONS`
- 替换命令输出中的所有中文术语
- 保持文件锁和原子操作逻辑
- 直接复用 `file_lock.py` 和 `utils.py`

### Phase 3: Dashboard 后端

**任务：** 移植 `server.py`

**输入：** `edict/dashboard/server.py`
**输出：** `ClassBrainAI/dashboard/server.py`

**修改要点：**
- 更新数据路径引用
- 修改 API 响应中的术语
- 保持所有端点逻辑不变
- 保持 CORS 和并发安全机制

### Phase 4: Dashboard 前端

**任务：** 移植 `dashboard.html`，应用校园风格 UI

**输入：** `edict/dashboard/dashboard.html`
**输出：** `ClassBrainAI/dashboard/dashboard.html`

**修改要点：**
- 替换颜色变量（CSS）
- 替换图标和装饰元素
- 替换所有显示文本
- 保持布局和交互逻辑
- 更新图表配色

---

## 6. 数据结构

### 任务数据格式 (tasks_source.json)

```json
{
  "id": "CB-20260322-001",
  "title": "任务标题",
  "state": "Monitor",
  "org": "班长",
  "official": "班长",
  "description": "任务描述",
  "now": "当前动态",
  "todos": ["计划1✅", "计划2🔄", "计划3"],
  "flow_log": [
    {"at": "2026-03-22T10:00:00", "from": "班主任", "to": "班长", "remark": "创建任务"}
  ],
  "createdAt": "2026-03-22T10:00:00",
  "updatedAt": "2026-03-22T10:05:00"
}
```

### 状态常量定义

```python
# 任务状态
STATES = [
    "Pending",           # 待处理
    "Monitor",           # 班长处理中
    "Study",             # 学习委员处理中
    "Chair",             # 班委主席审议中
    "Assigned",          # 已派发
    "Doing",             # 执行中
    "Review",            # 待审查
    "Done",              # 已完成
    "Cancelled",         # 已取消
    "Blocked"            # 已暂停
]

# 状态转换规则
_VALID_TRANSITIONS = {
    "Pending": ["Monitor"],
    "Monitor": ["Study"],
    "Study": ["Chair", "Monitor"],
    "Chair": ["Assigned", "Study"],
    "Assigned": ["Doing"],
    "Doing": ["Review", "Done"],
    "Review": ["Done", "Doing"],
    "Done": [],
    "Cancelled": [],
    "Blocked": ["Doing", "Cancelled"]
}
```

---

## 7. 技术栈

与 edict 保持一致：

- **后端：** Python 3.10+，纯标准库 HTTP 服务器
- **前端：** 原生 HTML/CSS/JavaScript（单文件看板）
- **数据：** JSON 文件 + 文件锁（并发安全）
- **可选：** React 18 + TypeScript + Vite（现代前端）

---

## 8. 国际化规划

- **当前版本：** 纯中文版
- **未来版本：** 英文版（独立开发，配置文件切换）

---

## 附录：命令速查

### class_board.py 命令

```bash
# 创建任务
python3 scripts/class_board.py create CB-20260322-001 "任务标题" Monitor 班长 班长

# 更新状态
python3 scripts/class_board.py state CB-20260322-001 Study "转学习委员处理"

# 流程日志
python3 scripts/class_board.py flow CB-20260322-001 "班长" "学习委员" "转交处理"

# 进度上报
python3 scripts/class_board.py progress CB-20260322-001 "正在分析需求" "分析🔄|规划|执行"

# 完成任务
python3 scripts/class_board.py done CB-20260322-001 "产出内容" "完成摘要"

# 暂停/恢复/取消
python3 scripts/class_board.py stop CB-20260322-001 "暂停原因"
python3 scripts/class_board.py resume CB-20260322-001
python3 scripts/class_board.py cancel CB-20260322-001 "取消原因"
```

---

**设计状态：** ✅ 已批准
**下一步：** 创建实施计划
