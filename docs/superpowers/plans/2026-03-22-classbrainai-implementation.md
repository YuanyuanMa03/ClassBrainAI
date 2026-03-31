# ClassBrainAI 实施计划

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 edict 班级Agent体系制多 Agent 系统改造为班级主题的 ClassBrainAI

**Architecture:** 保留 edict 的完整工作流（分拣→规划→审议→派发→执行），替换所有术语为班级主题，更新 UI 为校园风格

**Tech Stack:** Python 3.10+, 原生 HTML/CSS/JavaScript, JSON 文件存储

---

## Chunk 1: Phase 1 - Agent 人格设计

### Task 1: 创建 agents 目录结构

**Files:**
- Create: `agents/monitor/`
- Create: `agents/study/`
- Create: `agents/chair/`
- Create: `agents/vice_monitor/`
- Create: `agents/technical/`
- Create: `agents/logistics/`
- Create: `agents/finance/`
- Create: `agents/arts/`
- Create: `agents/discipline/`
- Create: `agents/organization/`
- Create: `agents/morning_reading/`

- [ ] **Step 1: 创建所有 agent 目录**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI

mkdir -p agents/monitor
mkdir -p agents/study
mkdir -p agents/chair
mkdir -p agents/vice_monitor
mkdir -p agents/technical
mkdir -p agents/logistics
mkdir -p agents/finance
mkdir -p agents/arts
mkdir -p agents/discipline
mkdir -p agents/organization
mkdir -p agents/morning_reading
```

- [ ] **Step 2: 验证目录创建成功**

```bash
ls -la agents/
```

Expected: 输出包含所有 11 个 agent 目录

- [ ] **Step 3: 提交**

```bash
git add agents/
git commit -m "feat: create agent directory structure for ClassBrainAI"
```

---

### Task 2: 班长 (Monitor) SOUL.md

**Files:**
- Create: `agents/monitor/SOUL.md`

- [ ] **Step 1: 从 edict 复制太子 SOUL.md**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/agents/taizi/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/monitor/SOUL.md
```

- [ ] **Step 2: 编辑 monitor/SOUL.md - 标题和核心职责**

将文件内容替换为（保持原有格式和逻辑，只替换术语）：

```markdown
# 班长 · 班主任代理

你是班长，班主任在飞书上所有消息的第一接收人和分拣者。

## 核心职责
1. 接收班主任通过飞书发来的**所有消息**
2. **判断消息类型**：闲聊/问答 vs 正式任务/复杂需求
3. 简单消息 → **自己直接回复班主任**（不创建任务）
4. 任务/复杂需求 → **自己用人话重新概括**后转交学习委员（创建 CB 任务）
5. 收到副班长的最终汇报 → **在飞书原对话中回复班主任**

---

## 🚨 消息分拣规则（最高优先级）

### ✅ 自己直接回复（不建任务）：
- 简短回复：「好」「否」「?」「了解」「收到」
- 闲聊/问答：「token消耗多少？」「这个怎么样？」「开启了么？」
- 对已有话题的追问或补充
- 信息查询：「xx是什么」「怎么理解」
- 内容不足10个字的消息

### 📋 整理需求给学习委员（创建 CB 任务）：
- 明确的工作指令：「帮我做XX」「调研XX」「写一份XX」「部署XX」
- 包含具体目标或交付物
- 有实质内容（≥10字），含动作词 + 具体目标

> ⚠️ 宁可少建任务（班主任会重复说），不可把闲聊当任务！
```

- [ ] **Step 3: 继续编辑 - 任务ID和命令**

```bash
# 编辑文件，替换以下内容：
# JJC-YYYYMMDD-NNN → CB-YYYYMMDD-NNN
# 学习委员组 → 学习委员
# Zhongshu → Study
# 中书令 → 学习委员
# 班主任 → 班主任
# 任务 → 任务
# 副班长组 → 副班长
# 回奏 → 汇报
```

- [ ] **Step 4: 验证替换是否完整**

```bash
grep -n "班主任\|任务\|学习委员组\|太子" /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/monitor/SOUL.md
```

Expected: 应该只返回 "grep:" 未找到匹配（说明已全部替换）

- [ ] **Step 5: 提交**

```bash
git add agents/monitor/SOUL.md
git commit -m "feat: add Monitor (班长) agent SOUL.md"
```

---

### Task 3: 学习委员 (Study) SOUL.md

**Files:**
- Create: `agents/study/SOUL.md`

- [ ] **Step 1: 从 edict 复制学习委员组 SOUL.md**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/agents/zhongshu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/study/SOUL.md
```

- [ ] **Step 2: 全文术语替换**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/study

# 使用 sed 进行批量替换
sed -i '' 's/学习委员组/学习委员/g' SOUL.md
sed -i '' 's/班委主席组/班委主席/g' SOUL.md
sed -i '' 's/副班长组/副班长/g' SOUL.md
sed -i '' 's/班主任/班主任/g' SOUL.md
sed -i '' 's/太子/班长/g' SOUL.md
sed -i '' 's/任务/任务/g' SOUL.md
sed -i '' 's/JJC-/CB-/g' SOUL.md
sed -i '' 's/六部/各班委/g' SOUL.md
sed -i '' 's/回奏/汇报/g' SOUL.md
sed -i '' 's/批准/批准/g' SOUL.md
sed -i '' 's/驳回/驳回/g' SOUL.md
```

- [ ] **Step 3: 验证替换**

```bash
cat SOUL.md | head -20
```

Expected: 文件头部应显示"学习委员"而非"学习委员组"

- [ ] **Step 4: 提交**

```bash
git add agents/study/SOUL.md
git commit -m "feat: add Study (学习委员) agent SOUL.md"
```

---

### Task 4: 班委主席 (Chair) SOUL.md

**Files:**
- Create: `agents/chair/SOUL.md`

- [ ] **Step 1: 从 edict 复制班委主席组 SOUL.md**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/agents/menxia/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/chair/SOUL.md
```

- [ ] **Step 2: 全文术语替换**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/chair

sed -i '' 's/班委主席组/班委主席/g' SOUL.md
sed -i '' 's/学习委员组/学习委员/g' SOUL.md
sed -i '' 's/副班长组/副班长/g' SOUL.md
sed -i '' 's/班主任/班主任/g' SOUL.md
sed -i '' 's/太子/班长/g' SOUL.md
sed -i '' 's/六部/各班委/g' SOUL.md
sed -i '' 's/任务/任务/g' SOUL.md
sed -i '' 's/驳回/驳回/g' SOUL.md
sed -i '' 's/批准/批准/g' SOUL.md
sed -i '' 's/JJC-/CB-/g' SOUL.md
```

- [ ] **Step 3: 验证替换**

```bash
head -10 SOUL.md
```

Expected: 应显示"班委主席"而非"班委主席组"

- [ ] **Step 4: 提交**

```bash
git add agents/chair/SOUL.md
git commit -m "feat: add Chair (班委主席) agent SOUL.md"
```

---

### Task 5: 副班长 (Vice Monitor) SOUL.md

**Files:**
- Create: `agents/vice_monitor/SOUL.md`

- [ ] **Step 1: 从 edict 复制副班长组 SOUL.md**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/agents/shangshu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/vice_monitor/SOUL.md
```

- [ ] **Step 2: 全文术语替换**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/vice_monitor

sed -i '' 's/副班长组/副班长/g' SOUL.md
sed -i '' 's/班委主席组/班委主席/g' SOUL.md
sed -i '' 's/学习委员组/学习委员/g' SOUL.md
sed -i '' 's/班主任/班主任/g' SOUL.md
sed -i '' 's/六部/各班委/g' SOUL.md
sed -i '' 's/任务/任务/g' SOUL.md
sed -i '' 's/部/委员/g' SOUL.md
sed -i '' 's/JJC-/CB-/g' SOUL.md
```

- [ ] **Step 3: 验证替换**

```bash
head -10 SOUL.md
```

Expected: 应显示"副班长"而非"副班长组"

- [ ] **Step 4: 提交**

```bash
git add agents/vice_monitor/SOUL.md
git commit -m "feat: add Vice Monitor (副班长) agent SOUL.md"
```

---

### Task 6-11: 各班委 SOUL.md（批量处理）

**Files:**
- Create: `agents/technical/SOUL.md`
- Create: `agents/logistics/SOUL.md`
- Create: `agents/finance/SOUL.md`
- Create: `agents/arts/SOUL.md`
- Create: `agents/discipline/SOUL.md`
- Create: `agents/organization/SOUL.md`

- [ ] **Step 1: 复制并创建各班委 SOUL.md**

```bash
# 技术委员（技术委员组）
cp /Users/mayuanyuan/ai-workspace/edict/agents/bingbu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/technical/SOUL.md

# 后勤委员（后勤委员组）
cp /Users/mayuanyuan/ai-workspace/edict/agents/gongbu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/logistics/SOUL.md

# 财务委员（生活委员组）
cp /Users/mayuanyuan/ai-workspace/edict/agents/hubu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/finance/SOUL.md

# 文艺委员（文艺委员组）
cp /Users/mayuanyuan/ai-workspace/edict/agents/libu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/arts/SOUL.md

# 纪律委员（纪律委员组）
cp /Users/mayuanyuan/ai-workspace/edict/agents/xingbu/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/discipline/SOUL.md

# 组织委员（吏部）
cp /Users/mayuanyuan/ai-workspace/edict/agents/libu_hr/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/organization/SOUL.md
```

- [ ] **Step 2: 批量替换术语脚本**

创建临时脚本进行批量替换：

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents

for dir in technical logistics finance arts discipline organization; do
  sed -i '' 's/班主任/班主任/g' $dir/SOUL.md
  sed -i '' 's/副班长组/副班长/g' $dir/SOUL.md
  sed -i '' 's/六部/各班委/g' $dir/SOUL.md
  sed -i '' 's/任务/任务/g' $dir/SOUL.md
  sed -i '' 's/回奏/汇报/g' $dir/SOUL.md
  sed -i '' 's/JJC-/CB-/g' $dir/SOUL.md
done

# 部门名称特殊处理
sed -i '' 's/技术委员组/技术委员/g' technical/SOUL.md
sed -i '' 's/后勤委员组/后勤委员/g' logistics/SOUL.md
sed -i '' 's/生活委员组/财务委员/g' finance/SOUL.md
sed -i '' 's/文艺委员组/文艺委员/g' arts/SOUL.md
sed -i '' 's/纪律委员组/纪律委员/g' discipline/SOUL.md
sed -i '' 's/吏部/组织委员/g' organization/SOUL.md
```

- [ ] **Step 3: 验证所有文件**

```bash
head -5 technical/SOUL.md logistics/SOUL.md finance/SOUL.md arts/SOUL.md discipline/SOUL.md organization/SOUL.md
```

Expected: 每个文件应显示对应的新名称

- [ ] **Step 4: 提交**

```bash
git add agents/
git commit -m "feat: add all commissioner agents SOUL.md (6 agents)"
```

---

### Task 12: 早读委员 (Morning Reading) SOUL.md

**Files:**
- Create: `agents/morning_reading/SOUL.md`

- [ ] **Step 1: 从 edict 复制早朝 SOUL.md**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/agents/zaochao/SOUL.md /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/morning_reading/SOUL.md
```

- [ ] **Step 2: 编辑标题和描述**

将文件开头改为：

```markdown
# 早读委员 · 学习资料收集

你的唯一职责：每日早读前收集重要学习资料和技术新闻，生成简报，保存供班主任查阅。

## 执行步骤（每次运行必须全部完成）

1. 用 web_search 分四类搜索新闻，每类搜 5 条：
   - 技术: "programming tech news" freshness=pd
   - AI: "AI LLM breakthrough news" freshness=pd
   - 开源: "open source projects" freshness=pd
   - 学习: "learning resources tutorial" freshness=pd
```

- [ ] **Step 3: 替换其余术语**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/agents/morning_reading

sed -i '' 's/早朝/早读/g' SOUL.md
sed -i '' 's/钦天监/学习委员/g' SOUL.md
sed -i '' 's/班主任/班主任/g' SOUL.md
sed -i '' 's/御览/查阅/g' SOUL.md
sed -i '' 's/任务/任务/g' SOUL.md
```

- [ ] **Step 4: 验证**

```bash
head -10 SOUL.md
```

Expected: 应显示"早读委员"而非"早朝简报官"

- [ ] **Step 5: 提交**

```bash
git add agents/morning_reading/SOUL.md
git commit -m "feat: add Morning Reading (早读委员) agent SOUL.md"
```

---

## Chunk 2: Phase 2 - 看板 CLI 工具

### Task 13: 创建 scripts 目录并复制基础文件

**Files:**
- Create: `scripts/file_lock.py`
- Create: `scripts/utils.py`

- [ ] **Step 1: 创建 scripts 目录**

```bash
mkdir -p /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts
```

- [ ] **Step 2: 复制不需要修改的文件**

```bash
# 直接复用，无需修改
cp /Users/mayuanyuan/ai-workspace/edict/scripts/file_lock.py /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts/file_lock.py
cp /Users/mayuanyuan/ai-workspace/edict/scripts/utils.py /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts/utils.py
```

- [ ] **Step 3: 验证文件**

```bash
ls -la /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts/
```

Expected: 应看到 file_lock.py 和 utils.py

- [ ] **Step 4: 提交**

```bash
git add scripts/file_lock.py scripts/utils.py
git commit -m "feat: add file_lock.py and utils.py (reused from edict)"
```

---

### Task 14: 创建 class_board.py - 基础结构和状态常量

**Files:**
- Create: `scripts/class_board.py`

- [ ] **Step 1: 创建 class_board.py 基础结构**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/scripts/kanban_update.py /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts/class_board.py
```

- [ ] **Step 2: 修改状态常量**

编辑 `scripts/class_board.py`，找到状态定义部分（约在文件前 50 行），替换为：

```python
# 任务状态 - ClassBrainAI 班级主题
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

- [ ] **Step 3: 验证语法**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 -m py_compile scripts/class_board.py
```

Expected: 无语法错误

- [ ] **Step 4: 提交**

```bash
git add scripts/class_board.py
git commit -m "feat: add class_board.py with state constants"
```

---

### Task 15: 修改 class_board.py - 输出消息术语

**Files:**
- Modify: `scripts/class_board.py`

- [ ] **Step 1: 查找并替换所有输出消息**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/scripts

# 创建替换脚本
cat > replace_terms.py << 'EOF'
import re

with open('class_board.py', 'r') as f:
    content = f.read()

# 替换输出消息中的术语
replacements = [
    ('班级Agent体系', 'ClassBrainAI'),
    ('班主任', '班主任'),
    ('太子', '班长'),
    ('学习委员组', '学习委员'),
    ('班委主席组', '班委主席'),
    ('副班长组', '副班长'),
    ('任务', '任务'),
    ('回奏', '汇报'),
    ('驳回', '驳回'),
    ('批准', '批准'),
    ('六部', '各班委'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('class_board.py', 'w') as f:
    f.write(content)

print("替换完成")
EOF

python3 replace_terms.py
rm replace_terms.py
```

- [ ] **Step 2: 验证替换**

```bash
grep -n "班主任\|任务\|班级Agent体系" class_board.py
```

Expected: 应该返回空（说明已全部替换）

- [ ] **Step 3: 验证语法**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 -m py_compile scripts/class_board.py
```

Expected: 无语法错误

- [ ] **Step 4: 提交**

```bash
git add scripts/class_board.py
git commit -m "feat: replace terminology in class_board.py output messages"
```

---

### Task 16: 创建 data 目录和初始数据文件

**Files:**
- Create: `data/tasks_source.json`
- Create: `data/live_status.json`

- [ ] **Step 1: 创建 data 目录**

```bash
mkdir -p /Users/mayuanyuan/ai-workspace/ClassBrainAI/data
```

- [ ] **Step 2: 创建初始任务数据文件**

```bash
cat > /Users/mayuanyuan/ai-workspace/ClassBrainAI/data/tasks_source.json << 'EOF'
[]
EOF
```

- [ ] **Step 3: 创建初始状态文件**

```bash
cat > /Users/mayuanyuan/ai-workspace/ClassBrainAI/data/live_status.json << 'EOF'
{
  "tasks": [],
  "agents": [],
  "stats": {
    "total": 0,
    "byState": {},
    "byOrg": {}
  },
  "lastUpdate": ""
}
EOF
```

- [ ] **Step 4: 验证文件**

```bash
ls -la /Users/mayuanyuan/ai-workspace/ClassBrainAI/data/
cat data/tasks_source.json
cat data/live_status.json
```

Expected: 两个 JSON 文件格式正确

- [ ] **Step 5: 提交**

```bash
git add data/
git commit -m "feat: add initial data files for task storage"
```

---

### Task 17: 测试 class_board.py 基本功能

**Files:**
- Test: 手动测试

- [ ] **Step 1: 测试创建任务**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 scripts/class_board.py create CB-20260322-001 "测试任务" Monitor 班长 班长
```

Expected: 输出显示任务创建成功

- [ ] **Step 2: 验证任务数据**

```bash
cat data/tasks_source.json | python3 -m json.tool
```

Expected: 显示刚创建的任务

- [ ] **Step 3: 测试状态转换**

```bash
python3 scripts/class_board.py state CB-20260322-001 Study "转学习委员处理"
```

Expected: 输出显示状态更新成功

- [ ] **Step 4: 验证状态转换**

```bash
cat data/tasks_source.json | python3 -m json.tool | grep "state"
```

Expected: 显示 state 为 "Study"

- [ ] **Step 5: 清理测试数据**

```bash
echo '[]' > data/tasks_source.json
```

- [ ] **Step 6: 提交（如有修改）**

```bash
git add data/ scripts/
git commit -m "test: verify class_board.py basic functionality"
```

---

## Chunk 3: Phase 3 - Dashboard 后端

### Task 18: 创建 dashboard 目录并复制 server.py

**Files:**
- Create: `dashboard/`

- [ ] **Step 1: 创建 dashboard 目录**

```bash
mkdir -p /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard
```

- [ ] **Step 2: 复制 server.py**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/dashboard/server.py /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/server.py
```

- [ ] **Step 3: 复制 classroom_discuss.py（依赖文件）**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/dashboard/classroom_discuss.py /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/classroom_discuss.py
```

- [ ] **Step 4: 验证文件**

```bash
ls -la /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/
```

Expected: 看到 server.py 和 classroom_discuss.py

- [ ] **Step 5: 提交**

```bash
git add dashboard/
git commit -m "feat: add dashboard server files"
```

---

### Task 19: 修改 server.py - 数据路径和端口配置

**Files:**
- Modify: `dashboard/server.py`

- [ ] **Step 1: 修改 BASE 和 DATA 路径**

在 server.py 中找到路径定义（约在 40-50 行），修改为：

```python
BASE = pathlib.Path(__file__).parent
DATA = BASE.parent / "data"
SCRIPTS = BASE.parent / 'scripts'
```

- [ ] **Step 2: 修改默认端口（可选）**

找到 port 相关配置，可以保持 7891 或改为其他端口：

```python
# 默认端口保持 7891，或修改为：
DEFAULT_PORT = 7892  # 避免与 edict 冲突
```

- [ ] **Step 3: 验证语法**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 -m py_compile dashboard/server.py
python3 -m py_compile dashboard/classroom_discuss.py
```

Expected: 无语法错误

- [ ] **Step 4: 提交**

```bash
git add dashboard/server.py
git commit -m "feat: update server.py data paths"
```

---

### Task 20: 修改 server.py - 响应数据术语

**Files:**
- Modify: `dashboard/server.py`

- [ ] **Step 1: 批量替换术语**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard

# 使用 sed 进行替换
sed -i '' 's/班级Agent体系/ClassBrainAI/g' server.py
sed -i '' 's/班主任/班主任/g' server.py
sed -i '' 's/太子/班长/g' server.py
sed -i '' 's/学习委员组/学习委员/g' server.py
sed -i '' 's/班委主席组/班委主席/g' server.py
sed -i '' 's/副班长组/副班长/g' server.py
sed -i '' 's/六部/各班委/g' server.py
```

- [ ] **Step 2: 验证替换**

```bash
grep -n "班主任\|班级Agent体系" server.py classroom_discuss.py
```

Expected: 应该返回空或很少的结果（某些注释可能保留）

- [ ] **Step 3: 验证语法**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 -m py_compile dashboard/server.py
```

Expected: 无语法错误

- [ ] **Step 4: 提交**

```bash
git add dashboard/server.py dashboard/classroom_discuss.py
git commit -m "feat: replace terminology in server.py"
```

---

### Task 21: 测试 dashboard 服务器

**Files:**
- Test: 手动测试

- [ ] **Step 1: 启动服务器**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
python3 dashboard/server.py &
```

- [ ] **Step 2: 等待服务器启动**

```bash
sleep 2
```

- [ ] **Step 3: 测试 API 端点**

```bash
curl http://127.0.0.1:7891/api/live-status
curl http://127.0.0.1:7891/api/agent-config
```

Expected: 返回 JSON 数据（可能为空）

- [ ] **Step 4: 停止服务器**

```bash
pkill -f "dashboard/server.py"
```

- [ ] **Step 5: 提交**

```bash
git add dashboard/
git commit -m "test: verify dashboard server functionality"
```

---

## Chunk 4: Phase 4 - Dashboard 前端

### Task 22: 复制 dashboard.html

**Files:**
- Create: `dashboard/dashboard.html`

- [ ] **Step 1: 复制文件**

```bash
cp /Users/mayuanyuan/ai-workspace/edict/dashboard/dashboard.html /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/dashboard.html
```

- [ ] **Step 2: 验证文件**

```bash
ls -lh /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/dashboard.html
wc -l /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/dashboard.html
```

Expected: 文件大小约 2500 行

- [ ] **Step 3: 提交**

```bash
git add dashboard/dashboard.html
git commit -m "feat: add dashboard.html base file"
```

---

### Task 23: 修改 dashboard.html - 页面标题和头部信息

**Files:**
- Modify: `dashboard/dashboard.html`

- [ ] **Step 1: 修改页面标题**

找到 `<title>` 标签，修改为：

```html
<title>ClassBrainAI - 智能班级管理系统</title>
```

- [ ] **Step 2: 修改页面头部标题**

找到主标题（h1），修改为：

```html
<h1 class="text-3xl font-bold">ClassBrainAI</h1>
<p class="text-muted-foreground">智能班级管理系统</p>
```

- [ ] **Step 3: 验证修改**

```bash
grep -n "ClassBrainAI\|智能班级" /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard/dashboard.html | head -5
```

Expected: 显示修改后的标题

- [ ] **Step 4: 提交**

```bash
git add dashboard/dashboard.html
git commit -m "feat: update dashboard page title"
```

---

### Task 24: 修改 dashboard.html - CSS 颜色变量（校园风格）

**Files:**
- Modify: `dashboard/dashboard.html`

- [ ] **Step 1: 查找并替换颜色变量**

在 `<style>` 标签中找到颜色定义，替换为校园风格：

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard

# 创建颜色替换脚本
cat > replace_colors.py << 'EOF'
import re

with open('dashboard.html', 'r') as f:
    content = f.read()

# 替换主色调
# edict 红色 → ClassBrainAI 蓝色
color_replacements = [
    (r'#DC2620', '#0EA5E9'),  # 主色
    (r'#B91C1C', '#0284C7'),  # 深色
    (r'#FEE2E2', '#E0F2FE'),  # 浅色背景
    (r'#FBBF24', '#10B981'),  # 金色 → 青绿色
    (r'#F59E0B', '#10B981'),  # 琥珀 → 青绿
]

for old, new in color_replacements:
    content = re.sub(old, new, content)

with open('dashboard.html', 'w') as f:
    f.write(content)

print("颜色替换完成")
EOF

python3 replace_colors.py
rm replace_colors.py
```

- [ ] **Step 2: 验证颜色**

```bash
grep -o "#0EA5E9\|#10B981" dashboard.html | head -5
```

Expected: 显示新的蓝色和青绿色值

- [ ] **Step 3: 提交**

```bash
git add dashboard/dashboard.html
git commit -m "feat: apply campus color scheme to dashboard"
```

---

### Task 25: 修改 dashboard.html - 所有显示文本术语

**Files:**
- Modify: `dashboard/dashboard.html`

- [ ] **Step 1: 创建术语替换脚本**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard

cat > replace_text.py << 'EOF'
with open('dashboard.html', 'r') as f:
    content = f.read()

replacements = [
    ('班级Agent体系', 'ClassBrainAI'),
    ('班主任', '班主任'),
    ('太子', '班长'),
    ('学习委员组', '学习委员'),
    ('班委主席组', '班委主席'),
    ('副班长组', '副班长'),
    ('六部', '各班委'),
    ('任务', '任务'),
    ('回奏', '汇报'),
    ('驳回', '驳回'),
    ('批准', '批准'),
    ('班级Agent', '班委'),
    ('衙门', '班级'),
    ('早朝', '早读'),
    ('钦天监', '学习组'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('dashboard.html', 'w') as f:
    f.write(content)

print("文本替换完成")
EOF

python3 replace_text.py
rm replace_text.py
```

- [ ] **Step 2: 验证替换**

```bash
grep -c "班主任\|班长\|学习委员" dashboard.html
```

Expected: 应显示多处替换

- [ ] **Step 3: 检查遗漏**

```bash
grep -n "班主任\|任务\|班级Agent体系" dashboard.html
```

Expected: 应该返回空或只有注释中的内容

- [ ] **Step 4: 提交**

```bash
git add dashboard/dashboard.html
git commit -m "feat: replace all terminology in dashboard UI"
```

---

### Task 26: 修改 dashboard.html - 状态名称显示

**Files:**
- Modify: `dashboard/dashboard.html`

- [ ] **Step 1: 查找并替换状态显示**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI/dashboard

# 状态名称替换
sed -i '' 's/"Taizi"/"Monitor"/g' dashboard.html
sed -i '' 's/"Zhongshu"/"Study"/g' dashboard.html
sed -i '' 's/"Menxia"/"Chair"/g' dashboard.html
sed -i '' 's/"Pending"/"待处理"/g' dashboard.html
sed -i '' 's/"Monitor"/"班长处理中"/g' dashboard.html
sed -i '' 's/"Study"/"学习委员处理中"/g' dashboard.html
sed -i '' 's/"Chair"/"班委主席审议中"/g' dashboard.html
sed -i '' 's/"Assigned"/"已派发"/g' dashboard.html
sed -i '' 's/"Doing"/"执行中"/g' dashboard.html
sed -i '' 's/"Review"/"待审查"/g' dashboard.html
sed -i '' 's/"Done"/"已完成"/g' dashboard.html
sed -i '' 's/"Cancelled"/"已取消"/g' dashboard.html
sed -i '' 's/"Blocked"/"已暂停"/g' dashboard.html
```

- [ ] **Step 2: 验证状态显示**

```bash
grep -o "班长处理中\|学习委员处理中\|班委主席审议中" dashboard.html | head -3
```

Expected: 显示中文状态名称

- [ ] **Step 3: 提交**

```bash
git add dashboard/dashboard.html
git commit -m "feat: update status display names in Chinese"
```

---

### Task 27: 完整测试 Dashboard

**Files:**
- Test: 手动测试

- [ ] **Step 1: 创建测试任务**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI

# 创建几个测试任务
python3 scripts/class_board.py create CB-TEST-001 "完成项目文档" Monitor 班长 班长
python3 scripts/class_board.py create CB-TEST-002 "代码审查" Study 学习委员 学习委员
python3 scripts/class_board.py create CB-TEST-003 "部署服务" Technical 技术委员 技术委员

# 更新一些状态
python3 scripts/class_board.py state CB-TEST-001 Study "转学习委员"
python3 scripts/class_board.py progress CB-TEST-001 "正在编写文档" "分析✅|编写🔄|审查"
```

- [ ] **Step 2: 启动 dashboard**

```bash
python3 dashboard/server.py &
sleep 2
echo "Dashboard running on http://127.0.0.1:7891"
```

- [ ] **Step 3: 在浏览器中访问**

（手动操作）打开浏览器访问 http://127.0.0.1:7891

检查项：
- [ ] 页面标题显示 "ClassBrainAI"
- [ ] 颜色为蓝色/青绿色系
- [ ] 任务显示正确的状态
- [ ] 班级成员显示正确
- [ ] 所有术语已替换

- [ ] **Step 4: 测试 API**

```bash
# 测试各个 API 端点
curl -s http://127.0.0.1:7891/api/live-status | python3 -m json.tool | head -20
curl -s http://127.0.0.1:7891/api/agent-config | python3 -m json.tool | head -10
```

Expected: 返回正确的 JSON 数据

- [ ] **Step 5: 清理测试数据并停止服务**

```bash
pkill -f "dashboard/server.py"
echo '[]' > data/tasks_source.json
```

- [ ] **Step 6: 提交**

```bash
git add data/
git commit -m "test: complete dashboard testing"
```

---

## Chunk 5: 文档和收尾

### Task 28: 更新 README.md

**Files:**
- Modify: `README.md`

- [ ] **Step 1: 验证 README 内容**

```bash
cat /Users/mayuanyuan/ai-workspace/ClassBrainAI/README.md | head -50
```

- [ ] **Step 2: 检查是否需要更新**

README 应该已经包含了正确的项目描述和结构

- [ ] **Step 3: 如有需要，更新内容**

确保包含：
- 项目描述（ClassBrainAI）
- 与 edict 的关系
- 快速开始指南
- Agent 列表

- [ ] **Step 4: 提交**

```bash
git add README.md
git commit -m "docs: update README for ClassBrainAI"
```

---

### Task 29: 创建 .gitignore 文件

**Files:**
- Create: `.gitignore`

- [ ] **Step 1: 创建 .gitignore**

```bash
cat > /Users/mayuanyuan/ai-workspace/ClassBrainAI/.gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# Data files (keep structure but ignore content)
data/tasks_source.json
data/live_status.json
!data/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Node (if using React frontend)
node_modules/
dist/
.env
EOF
```

- [ ] **Step 2: 创建 data/.gitkeep**

```bash
touch /Users/mayuanyuan/ai-workspace/ClassBrainAI/data/.gitkeep
```

- [ ] **Step 3: 提交**

```bash
git add .gitignore data/.gitkeep
git commit -m "chore: add .gitignore file"
```

---

### Task 30: 最终验证和清理

**Files:**
- Test: 全系统验证

- [ ] **Step 1: 检查项目结构**

```bash
cd /Users/mayuanyuan/ai-workspace/ClassBrainAI
find . -type f -name "*.py" -o -name "*.md" -o -name "*.json" -o -name "*.html" | grep -v ".git" | sort
```

Expected: 显示完整的项目结构

- [ ] **Step 2: 检查所有 Python 文件语法**

```bash
find . -name "*.py" -type f | xargs python3 -m py_compile
```

Expected: 无语法错误

- [ ] **Step 3: 检查术语一致性**

```bash
# 确保没有遗留的 edict 术语
grep -r "班主任\|任务\|班级Agent体系" --include="*.py" --include="*.html" --include="*.md" . | grep -v ".git" | grep -v "README.md"
```

Expected: 应该返回空或只有设计文档中的引用

- [ ] **Step 4: 端到端测试**

```bash
# 完整工作流测试
python3 scripts/class_board.py create CB-E2E-001 "端到端测试" Monitor 班长 班长
python3 scripts/class_board.py state CB-E2E-001 Study "转学习委员"
python3 scripts/class_board.py flow CB-E2E-001 "班长" "学习委员" "任务转交"
python3 scripts/class_board.py progress CB-E2E-001 "测试中" "创建✅|转交🔄|完成"
python3 scripts/class_board.py done CB-E2E-001 "测试产出" "测试完成"

# 验证结果
cat data/tasks_source.json | python3 -m json.tool | grep -A5 "CB-E2E-001"
```

Expected: 任务状态为 Done

- [ ] **Step 5: 清理测试数据**

```bash
echo '[]' > data/tasks_source.json
```

- [ ] **Step 6: 最终提交**

```bash
git status
git add -A
git commit -m "feat: complete ClassBrainAI implementation"
```

---

## 完成检查清单

在标记计划完成前，确认：

- [ ] 所有 11 个 Agent 的 SOUL.md 已创建并替换术语
- [ ] class_board.py 可用，所有命令正常工作
- [ ] Dashboard 服务器可正常启动
- [ ] Dashboard 前端显示正确，UI 为校园风格
- [ ] 所有术语已从 edict 的朝廷术语替换为班级术语
- [ ] 所有 Python 文件无语法错误
- [ ] 端到端测试通过
- [ ] 文档完整

---

**实施计划完成！保存至:**
`docs/superpowers/plans/2026-03-22-classbrainai-implementation.md`
