# ClassBrainAI / ClassBrainAI · 智能班级管理系统

> 基于多 Agent 协作的班级管理系统，让 AI 成为班主任和同学们的得力助手

---

## 🎓 核心功能

### 1. 班级角色系统
- 班长（Monitor）- 班主任代理，负责任务分拣和协调
- 副班长（Vice Monitor）- 协助班长处理日常事务
- 班委主席（Chair）- 协调各班委工作，主持班委会
- 学习委员（Study）- 负责学习相关事务
- 早读委员（Morning Reading）- 组织和管理早读活动
- 文艺委员（Arts）- 组织文艺活动和班级文化建设
- 纪律委员（Discipline）- 维护班级纪律和秩序
- 生活委员（Finance）- 管理班级财务和生活事务
- 后勤委员（Logistics）- 负责后勤保障和物资管理
- 组织委员（Organization）- 组织班级活动和人员协调
- 技术委员（Technical）- 负责技术支持和系统维护

### 2. 智能任务管理
- 任务创建和分配
- 进度跟踪和汇报
- 自动归档到知识库

### 3. 知识库系统
- 学习资料管理
- 活动方案存档
- 管理经验积累
- 知识检索和推荐

### 4. 实时看板
- 任务状态可视化
- 班级运营数据
- 活动时间线

---

## 🚀 技术栈

### 后端
- Python 3.10+
- Flask (轻量级 Web 框架)
- JSON 数据存储

### 前端
- HTML5 + CSS3
- 原生 JavaScript
- 响应式设计

### AI 集成
- OpenAI API (GPT-4)
- Claude API
- Multi-Agent 架构

---

## 📁 项目结构

```
ClassBrainAI/
├── README.md                    # 项目说明
├── agents/                      # AI 角色定义（各班委）
│   ├── arts/                   # 文艺委员
│   ├── chair/                  # 班委主席
│   ├── discipline/             # 纪律委员
│   ├── finance/                # 生活委员
│   ├── logistics/              # 后勤委员
│   ├── monitor/                # 班长
│   ├── morning_reading/        # 早读委员
│   ├── organization/           # 组织委员
│   ├── study/                  # 学习委员
│   ├── technical/              # 技术委员
│   └── vice_monitor/           # 副班长
├── config/                      # 配置文件
├── dashboard/                   # 实时看板
│   ├── server.py               # 看板服务器
│   ├── court_discuss.py        # 议事厅讨论
│   └── dashboard.html          # 看板前端界面
├── data/                        # 数据存储
│   ├── tasks_source.json       # 任务数据源
│   └── live_status.json        # 实时状态
├── docs/                        # 文档
├── scripts/                     # 工具脚本
│   ├── class_board.py          # 班委会核心逻辑
│   ├── utils.py                # 工具函数
│   └── file_lock.py            # 文件锁机制
└── src/                         # 核心模块
```

---

## 🎯 核心设计原则

### 1. 真实性优先
- 模拟真实班级的管理场景
- 角色职责贴近实际
- 工作流程符合班级运作

### 2. 可用性优先
- 简洁直观的界面
- 高效的任务处理流程
- 智能化的辅助功能

### 3. 可扩展性优先
- 模块化的代码结构
- 清晰的接口定义
- 灵活的配置系统

### 4. 可维护性优先
- 完善的文档
- 充分的测试覆盖
- 清晰的代码规范

---

## 📈 发展路线图

### Phase 1：核心功能（MVP）
- [x] 基础项目结构
- [ ] 班级角色系统
- [ ] 智能任务管理
- [ ] 知识库系统

### Phase 2：高级功能
- [ ] 实时看板
- [ ] 自动化工作流
- [ ] 班级数据分析

### Phase 3：生态建设
- [ ] 插件系统
- [ ] 第三方集成
- [ ] 开放 API

---

## 🚀 快速开始

### 安装
```bash
git clone https://github.com/YuanyuanMa03/ClassBrainAI.git
cd ClassBrainAI
```

### 运行
```bash
# 启动看板服务器
cd dashboard
python server.py

# 访问看板
# 在浏览器中打开: http://localhost:5000
```

### 使用班委会系统
```bash
# 运行班委会核心逻辑
cd scripts
python class_board.py
```

---

## 📚 文档

- [架构文档](./docs/architecture.md)
- [API 文档](./docs/api.md)
- [部署文档](./docs/deployment.md)
- [用户指南](./docs/user_guide.md)

---

## 🤝 贡献指南

欢迎贡献代码、文档、Bug 报告或新功能建议！

1. Fork 本仓库
2. 创建功能分支
3. 提交 Pull Request
4. 遵循代码规范

---

## 📄 许可证

本项目采用 MIT 许可证。

---

## 👥 联系方式

- **GitHub:** https://github.com/YuanyuanMa03/ClassBrainAI
- **Issues:** https://github.com/YuanyuanMa03/ClassBrainAI/issues
- **Discussions:** https://github.com/YuanyuanMa03/ClassBrainAI/discussions

---

## 🎉 致谢

本项目灵感来源于以下优秀的开源项目：
- **edict** (cft0808/edict) - 基于三省六部制的 Multi-Agent 架构，为 ClassBrainAI 的班级管理架构提供了重要参考
- **MindOS** (YuanyuanMa03/MindOS) - 知识库管理系统
- **OpenClaw** (openclaw/openclaw) - Personal AI Assistant

ClassBrainAI 将 edict 的古代三省六部制创新性地转化为现代班级管理架构，让 AI 班委们协同工作，实现智能化的班级管理。

感谢开源社区的无私奉献！

---

**ClassBrainAI** - 让 AI 成为班级管理的得力助手 🎓🤖🚀
