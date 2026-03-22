# ClassBrainAI / ClassBrainAI · 智能班级管理系统

> 基于多 Agent 协作的班级管理系统，让 AI 成为班主任和同学们的得力助手

---

## 🎓 核心功能

### 1. 班级角色系统
- 班长（班主任代理） - 任务分拣和协调
- 班委（学习、文艺、体育等）- 各司其职
- 班委主席 - 协调各班委工作

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
- FastAPI 0.100+
- SQLAlchemy 2.0+
- PostgreSQL 14+

### 前端
- React 18
- TypeScript 5+
- Vite 4.0+
- Tailwind CSS 3.4+
- shadcn/ui

### AI 集成
- OpenAI API
- Claude 3.7
- Pinecone（向量数据库）

---

## 📁 项目结构

```
ClassBrainAI/
├── README.md               # 项目说明
├── requirements.txt          # 依赖列表
├── setup.py               # 安装脚本
├── .env.example            # 环境变量示例
├── src/
│   ├── core/          # 核心模块
│   │   ├── models/    # 数据模型
│   │   ├── schemas/   # Pydantic 模型
│   │   ├── database/  # 数据库操作
│   │   ├── services/   # 业务服务
│   ├── agents/       # AI 角色定义
│   ├── tasks/        # 任务管理
│   └── kanban/      # 看板系统
│   ├── api/          # API 路由
│   │   ├── main.py   # FastAPI 主入口
│   │   ├── routers/  # API 路由
│   │   └── deps/    # 依赖
│   ├── dashboard/    # 看板前端
│   │   ├── App.tsx
│   │   ├── components/
│   │   ├── hooks/
│   │   └── pages/
│   ├── knowledge/    # 知识库系统
│   │   ├── client/  # 知识库客户端
│   │   ├── models/  # 知识库模型
│   │   └── services/ # 知识库服务
│   ├── llm/         # LLM 集成
│   │   ├── providers/ # 模型提供商
│   │   └── utils/     # 工具函数
└── tests/             # 测试文件
    ├── test_api/
    ├── test_agents/
    ├── test_tasks/
    └── test_knowledge/
├── docs/              # 文档
│   ├── architecture.md   # 架构文档
│   ├── api.md          # API 文档
│   ├── deployment.md    # 部署文档
│   └── user_guide.md   # 用户指南
├── config/            # 配置文件
│   ├── settings.py   # 配置管理
│   └── logging.yaml  # 日志配置
├── scripts/           # 工具脚本
│   ├── setup.sh       # 安装脚本
│   ├── migrate.sh     # 数据库迁移
│   └── backup.sh       # 备份脚本
└── deployment/         # 部署配置
    ├── Dockerfile
    ├── docker-compose.yml
    └── .github/workflows/
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
pip install -r requirements.txt
python setup.py
```

### 运行
```bash
# 启动后端
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

# 启动前端（开发模式）
npm run dev

# 启动前端（生产模式）
npm run build
npm run preview
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
- **edict** (cft0808/edict) - 三省六部制 Multi-Agent 架构
- **MindOS** (YuanyuanMa03/MindOS) - 知识库管理
- **OpenClaw** (openclaw/openclaw) - Personal AI Assistant

感谢开源社区的无私奉献！

---

**ClassBrainAI** - 让 AI 成为班级管理的得力助手 🎓🤖🚀
