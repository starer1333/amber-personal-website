from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent

st.set_page_config(
    page_title="Amber Wang Portfolio",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="collapsed",
)


I18N = {
    "中文": {
        "nav": ["首页", "关于", "项目", "AI Lab", "简历", "联系"],
        "lang_label": "Language / 语言",
        "hero_eyebrow": "会计 x 商业分析 x AI 工作流",
        "hero_title": "Amber Wang",
        "hero_subtitle": (
            "我关注审计 / 会计、行业研究 / 咨询、AI x 财务 / AI x 业务分析，也保留 HRBP / "
            "People Operations 方向可能性。我的核心优势是把复杂业务信息结构化，把重复流程工具化，"
            "把研究成果可视化。"
        ),
        "view_projects": "查看项目",
        "download_resume": "下载简历",
        "chips": ["Audit & Accounting", "Business Research", "AI x Finance", "People Operations"],
        "metrics": [
            ("8", "覆盖审计、商业研究、AI 和产品原型的作品集项目"),
            ("30+", "实习期间支持的企业函证流程案例"),
            ("4", "核心方向：会计审计、行业研究、AI 工作流、People Ops"),
        ],
        "about_title": "关于我",
        "about_lead": (
            "我是一名会计学本科生，正在构建 Accounting、Business Research、AI Tools 和 "
            "People Operations 的复合能力组合。"
        ),
        "pillars": [
            (
                "Accounting & Audit Foundation",
                "理解审计流程、财务数据处理和底稿逻辑，能把重复事项整理成清晰流程。",
                ["Audit", "Excel", "VBA"],
            ),
            (
                "Business Research Thinking",
                "用咨询式结构拆解行业、公司、商业模式和财务表现，输出可展示的结论页。",
                ["Research", "Strategy", "PPT"],
            ),
            (
                "AI-enabled Workflow Builder",
                "探索用 AI-assisted coding、LLM API 和知识库工具处理非结构化业务材料。",
                ["Python", "Streamlit", "LLM"],
            ),
        ],
        "featured_title": "精选项目",
        "featured_lead": "首页只展示最能代表求职主线的三个项目：AI 财务工具、审计函证流程、战略财务分析。",
        "projects_title": "项目作品集",
        "projects_lead": (
            "每个项目都用 Problem -> Method -> Output -> Value 的四步逻辑图呈现，方便 HR 和面试官快速判断项目价值。"
        ),
        "all": "全部",
        "category_label": "项目分类",
        "details": "展开项目详情",
        "my_role": "我的角色",
        "deliverables": "产出物",
        "target_roles": "适配岗位",
        "download_pdf": "下载作品",
        "pdf_missing": "PDF 待补充",
        "view_github": "查看 GitHub",
        "view_demo": "查看 Demo",
        "ai_lab_title": "AI & Coding Lab",
        "ai_lab_lead": "我正在用 AI-assisted coding，把财务分析、业务流程、知识库和小程序原型转化为可展示、可复用的工具。",
        "ai_modules": [
            ("AI 财务文本分析", "财务文本输入 -> LLM 摘要与字段提取 -> 结构化输出 -> 人工复核"),
            ("Prompt Engineering", "把模糊业务问题转化为稳定输出格式和可复用提示词模板"),
            ("Streamlit Data Tool", "用低代码方式快速搭建财务数据录入、分析和可视化页面"),
            ("City Pizza Mini Program", "从点餐流程到商家后台，展示产品结构和 AI 辅助开发能力"),
        ],
        "resume_title": "简历",
        "resume_lead": "你可以在这里下载我的最新版简历。",
        "resume_button": "下载最新版简历",
        "resume_missing": "请将最新版简历放到 assets/resume/resume_latest.pdf，页面会自动显示下载按钮。",
        "resume_cards": [
            ("Audit / Accounting", "Audit workflow · Excel automation · Financial data"),
            ("Business Research", "Industry research · Strategy deck · Financial analysis"),
            ("AI x Finance", "LLM workflow · Streamlit · Structured output"),
        ],
        "contact_title": "欢迎联系我。",
        "contact_lead": "我正在寻找审计 / 会计、行业研究 / 咨询、AI x 财务 / AI x 业务分析相关实习机会。",
        "footer": "Built with Streamlit · Designed as a career portfolio · 2026",
    },
    "English": {
        "nav": ["Home", "About", "Projects", "AI Lab", "Resume", "Contact"],
        "lang_label": "Language / 语言",
        "hero_eyebrow": "Accounting x Business Analysis x AI Workflow",
        "hero_title": "Amber Wang",
        "hero_subtitle": (
            "I am interested in audit, accounting, business research, consulting, AI x finance, "
            "and AI-enabled business analysis, while keeping an open path toward HRBP and People Operations. "
            "My core strength is turning complex business information into structured analysis, repeatable workflows, "
            "and clear portfolio-ready outputs."
        ),
        "view_projects": "View Projects",
        "download_resume": "Download Resume",
        "chips": ["Audit & Accounting", "Business Research", "AI x Finance", "People Operations"],
        "metrics": [
            ("8", "Portfolio projects across audit, research, AI and product"),
            ("30+", "Audit confirmation cases supported during internship"),
            ("4", "Core directions: accounting, research, AI workflow, people ops"),
        ],
        "about_title": "About",
        "about_lead": (
            "I am an accounting undergraduate building a cross-functional skill set across accounting, "
            "business research, AI tools and people operations."
        ),
        "pillars": [
            (
                "Accounting & Audit Foundation",
                "I understand audit workflows, financial data processing and documentation logic, and can turn repetitive tasks into clear processes.",
                ["Audit", "Excel", "VBA"],
            ),
            (
                "Business Research Thinking",
                "I structure industry, company, business model and financial analysis in a consulting-style way.",
                ["Research", "Strategy", "PPT"],
            ),
            (
                "AI-enabled Workflow Builder",
                "I explore AI-assisted coding, LLM APIs and knowledge-base tools to process unstructured business materials.",
                ["Python", "Streamlit", "LLM"],
            ),
        ],
        "featured_title": "Featured Projects",
        "featured_lead": "Three projects that best represent my career story: an AI finance tool, audit workflow work and strategic financial analysis.",
        "projects_title": "Projects",
        "projects_lead": "Each project uses a Problem -> Method -> Output -> Value logic map so recruiters can understand the project value quickly.",
        "all": "All",
        "category_label": "Project Category",
        "details": "Project Details",
        "my_role": "My Role",
        "deliverables": "Deliverables",
        "target_roles": "Target Roles",
        "download_pdf": "Download PDF",
        "pdf_missing": "PDF pending",
        "view_github": "GitHub",
        "view_demo": "Live Demo",
        "ai_lab_title": "AI & Coding Lab",
        "ai_lab_lead": "I use AI-assisted coding to turn finance analysis, business workflows, knowledge bases and mini-program prototypes into reusable tools.",
        "ai_modules": [
            ("AI Financial Text Analysis", "Financial text input -> LLM summary and field extraction -> structured output -> human review"),
            ("Prompt Engineering", "Turning ambiguous business questions into stable output formats and reusable prompt templates"),
            ("Streamlit Data Tool", "Rapidly building financial data input, analysis and visualization pages"),
            ("City Pizza Mini Program", "Showing product structure and AI-assisted development from ordering flow to merchant backend"),
        ],
        "resume_title": "Resume",
        "resume_lead": "Download my latest resume here.",
        "resume_button": "Download Latest Resume",
        "resume_missing": "Place the latest resume at assets/resume/resume_latest.pdf and the download button will appear automatically.",
        "resume_cards": [
            ("Audit / Accounting", "Audit workflow · Excel automation · Financial data"),
            ("Business Research", "Industry research · Strategy deck · Financial analysis"),
            ("AI x Finance", "LLM workflow · Streamlit · Structured output"),
        ],
        "contact_title": "Let's Connect.",
        "contact_lead": "I am looking for internship opportunities in audit, accounting, business research, consulting, AI x finance and AI-enabled business analysis.",
        "footer": "Built with Streamlit · Designed as a career portfolio · 2026",
    },
}


PROJECTS = {
    "中文": [
        {
            "name": "审计函证流程与 AI 辅助数据处理",
            "category": "Audit & Accounting",
            "summary": "在天职国际函证中心实习期间，参与 30+ 企业函证流程管理，并使用 Excel、VBA 与 DeepSeek 优化重复性数据处理流程。",
            "logic": {
                "Problem": "函证流程存在大量重复整理、状态跟踪和异常核验工作",
                "Method": "用 Excel、VBA 和 AI 工具辅助数据清洗与模板化处理",
                "Output": "形成进度统计、批量命名脚本和常见问题知识库探索",
                "Value": "提升流程透明度，支持项目经理更快定位异常事项",
            },
            "tools": ["Excel", "VBA", "DeepSeek", "Dify", "Audit Workflow"],
            "role": "负责回函数据整理、异常工单跟踪，并协调项目经理和银行人员。",
            "deliverables": ["脱敏流程总结", "函证进度统计", "自动化处理模板"],
            "target_roles": ["审计", "会计", "财务共享"],
            "download_file": "assets/projects/audit_confirmation_summary.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "IPO 企业盈余管理研究",
            "category": "Audit & Accounting",
            "summary": "基于 2011-2024 年 A 股 IPO 公司样本，研究审计师行业专长是否能够抑制 IPO 企业应计盈余管理。",
            "logic": {
                "Problem": "IPO 企业可能存在美化上市业绩和盈余操纵动机",
                "Method": "用修正 Jones 模型测度 AbsDA，并构建审计师行业专长变量",
                "Output": "完成固定效应回归、工具变量和机制分析",
                "Value": "解释审计供给能力对 IPO 盈余质量的治理作用",
            },
            "tools": ["CSMAR", "Stata", "Modified Jones", "Fixed Effects"],
            "role": "完成文献梳理、变量设计、模型构建和实证结果解释。",
            "deliverables": ["研究论文", "变量定义表", "Stata do 文件"],
            "target_roles": ["审计", "会计研究", "数据分析"],
            "download_file": "assets/projects/ipo_earnings_management.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "大众汽车集团行业研究与战略财务分析",
            "category": "Business Research",
            "summary": "以大众汽车集团为对象，分析收入横盘、利润率下滑、中国市场压力和软件转型瓶颈，形成咨询式分析 deck。",
            "logic": {
                "Problem": "传统车企在电动化和软件定义汽车时代面临利润质量修复压力",
                "Method": "拆解行业价值池、竞争格局、利润率变化和中国市场压力",
                "Output": "形成战略财务分析 deck 与利润率修复建议",
                "Value": "把复杂行业变化转化为可讨论的战略财务判断",
            },
            "tools": ["Annual Report", "Profit Bridge", "DuPont", "PPT"],
            "role": "拆解行业趋势、竞争格局、利润变化和软件平台瓶颈。",
            "deliverables": ["战略财务分析 deck", "核心结论页", "利润率修复建议"],
            "target_roles": ["行业研究", "咨询", "战略分析"],
            "download_file": "assets/projects/volkswagen_research.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "陕西文旅 IPO 商业分析",
            "category": "Business Research",
            "summary": "围绕陕西旅游文化产业股份有限公司 IPO，分析文旅行业增长、核心资产壁垒、演艺与索道业务模型。",
            "logic": {
                "Problem": "如何判断文旅公司的 IPO 投资价值和商业壁垒",
                "Method": "拆解行业增长、西安流量、文化 IP 和核心业务结构",
                "Output": "形成 IPO 商业分析 deck 与盈利质量判断",
                "Value": "帮助快速理解文旅资产的流量转化和上市故事",
            },
            "tools": ["Prospectus", "Business Model", "Financial Analysis", "PPT"],
            "role": "分析行业趋势、城市流量、核心业务和盈利质量。",
            "deliverables": ["IPO 商业分析 deck", "核心资产业务拆解"],
            "target_roles": ["咨询", "投研", "商业分析"],
            "download_file": "assets/projects/shaanxi_tourism_ipo.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "好利来营销策划案",
            "category": "Business Research",
            "summary": "以好利来为研究对象，围绕品牌年轻化、IP 联名、消费者行为和 4P 策略进行系统分析。",
            "logic": {
                "Problem": "高频 IP 联名带来流量，也可能造成审美疲劳和品牌资产弱化",
                "Method": "结合 PEST、SWOT、STP、4P 和消费者行为分析",
                "Output": "形成营销策划报告与品牌策略建议",
                "Value": "把品牌热度问题转化为可落地的营销优化路径",
            },
            "tools": ["PEST", "SWOT", "STP", "4P", "Consumer Analysis"],
            "role": "分析品牌背景、消费者行为、竞品格局和营销问题。",
            "deliverables": ["营销策划报告", "消费者分析", "品牌策略建议"],
            "target_roles": ["市场", "咨询", "商业分析"],
            "download_file": "assets/projects/holiland_marketing.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "AI + 财务数据分析网站",
            "category": "AI x Finance",
            "summary": "基于 Streamlit 搭建轻量级财务数据工具网站，调用大语言模型 API，对财务文本进行摘要和结构化输出。",
            "logic": {
                "Problem": "财务场景中存在大量非结构化文本和重复阅读成本",
                "Method": "使用 LLM API 与 Prompt 进行摘要、字段提取和格式约束",
                "Output": "生成结构化结果、关键信息摘要和可视化展示",
                "Value": "辅助人工复核，让财务信息处理更快、更清晰",
            },
            "tools": ["Streamlit", "Python", "LLM API", "Prompt Engineering"],
            "role": "设计网站功能、Prompt 输出格式、数据清洗流程和展示页面。",
            "deliverables": ["Live Demo", "结构化输出模板", "项目说明 PDF"],
            "target_roles": ["AI 财务", "业务分析", "数据分析"],
            "download_file": "assets/projects/ai_finance_website.pdf",
            "github_url": "",
            "demo_url": "https://auditflow13.streamlit.app/",
        },
        {
            "name": "AGI 引入对公司治理效果的影响研究",
            "category": "AI x Finance",
            "summary": "研究 AGI 引入是否能够改善上市公司治理效果，关注盈余管理、信息披露质量、高管薪酬和关联交易。",
            "logic": {
                "Problem": "AI / AGI 是否能缓解管理层信息优势并改善公司治理",
                "Method": "基于年报 MD&A 文本构建 AGI 关键词词典并匹配治理变量",
                "Output": "完成技术路线、变量设计和面板回归框架",
                "Value": "把 AI 战略文本转化为可检验的公司治理研究变量",
            },
            "tools": ["Python", "Text Mining", "Stata", "CSMAR", "Wind"],
            "role": "参与研究框架设计、理论机制推导、关键词词典构建和数据处理。",
            "deliverables": ["项目申请书", "答辩 PPT", "变量设计"],
            "target_roles": ["学术研究", "AI 商业分析", "数据分析"],
            "download_file": "assets/projects/agi_governance_research.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "City Pizza 微信点餐小程序",
            "category": "Product & Coding",
            "summary": "使用 AI 辅助开发微信点餐小程序原型，包含用户端点餐流程与商家端菜品、订单、会员和报表管理。",
            "logic": {
                "Problem": "小型餐饮门店需要可配置的点餐、商品和订单管理工具",
                "Method": "设计用户端购买路径和商家端管理模块",
                "Output": "完成小程序原型、商品规格管理和后台页面结构",
                "Value": "展示从业务流程到产品原型的 AI-assisted coding 能力",
            },
            "tools": ["WeChat Mini Program", "JavaScript", "WXML", "WXSS", "GitHub"],
            "role": "设计页面结构、业务流程、商家后台模块和商品管理逻辑。",
            "deliverables": ["小程序原型", "商家后台页面", "GitHub 仓库"],
            "target_roles": ["产品", "运营", "AI-assisted Coding"],
            "download_file": "assets/projects/city_pizza_miniprogram.pdf",
            "github_url": "https://github.com/starer1333/CSPS-mini-program",
            "demo_url": "",
        },
    ],
    "English": [
        {
            "name": "Audit Confirmation Workflow with AI-assisted Data Processing",
            "category": "Audit & Accounting",
            "summary": "During my internship at Baker Tilly China, I supported 30+ audit confirmation workflows and used Excel, VBA and DeepSeek to improve repetitive data-processing tasks.",
            "logic": {
                "Problem": "Audit confirmation work involves repeated sorting, status tracking and exception checks",
                "Method": "Used Excel, VBA and AI tools to clean data and standardize templates",
                "Output": "Built progress summaries, batch renaming logic and FAQ knowledge-base exploration",
                "Value": "Improved process visibility and helped managers identify exceptions faster",
            },
            "tools": ["Excel", "VBA", "DeepSeek", "Dify", "Audit Workflow"],
            "role": "Organized returned confirmation data, tracked exception tickets and coordinated with project managers and bank staff.",
            "deliverables": ["Sanitized process summary", "Confirmation progress tracker", "Automation templates"],
            "target_roles": ["Audit", "Accounting", "Shared Services"],
            "download_file": "assets/projects/audit_confirmation_summary.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "IPO Earnings Management Research",
            "category": "Audit & Accounting",
            "summary": "Using 2011-2024 A-share IPO samples, this research studies whether auditor industry specialization can restrain accrual-based earnings management.",
            "logic": {
                "Problem": "IPO firms may have incentives to beautify performance before listing",
                "Method": "Measured AbsDA with the Modified Jones model and built auditor specialization variables",
                "Output": "Completed fixed-effects regression, IV tests and mechanism analysis",
                "Value": "Explains how audit supply capability may improve IPO earnings quality",
            },
            "tools": ["CSMAR", "Stata", "Modified Jones", "Fixed Effects"],
            "role": "Completed literature review, variable design, model construction and empirical interpretation.",
            "deliverables": ["Research paper", "Variable definition table", "Stata do file"],
            "target_roles": ["Audit", "Accounting Research", "Data Analysis"],
            "download_file": "assets/projects/ipo_earnings_management.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "Volkswagen Industry Research and Strategic Financial Analysis",
            "category": "Business Research",
            "summary": "A consulting-style deck analyzing Volkswagen's flat revenue, declining margin, China market pressure and software transition bottlenecks.",
            "logic": {
                "Problem": "Legacy automakers face margin repair pressure in the EV and software-defined vehicle era",
                "Method": "Analyzed industry value migration, competition, margin changes and China market pressure",
                "Output": "Built a strategic financial analysis deck with margin recovery recommendations",
                "Value": "Turns complex industry shifts into clear strategic and financial judgment",
            },
            "tools": ["Annual Report", "Profit Bridge", "DuPont", "PPT"],
            "role": "Analyzed industry trends, competitive landscape, margin movement and software-platform bottlenecks.",
            "deliverables": ["Strategic financial analysis deck", "Executive summary pages", "Margin repair recommendations"],
            "target_roles": ["Industry Research", "Consulting", "Strategy"],
            "download_file": "assets/projects/volkswagen_research.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "Shaanxi Tourism IPO Business Analysis",
            "category": "Business Research",
            "summary": "An IPO-oriented business analysis of Shaanxi Tourism, covering tourism growth, asset barriers, performance business and cableway operations.",
            "logic": {
                "Problem": "How to evaluate the IPO value and business moat of a cultural tourism company",
                "Method": "Analyzed industry growth, Xi'an traffic, cultural IP and core business structure",
                "Output": "Built an IPO business analysis deck and profitability-quality view",
                "Value": "Clarifies how tourism assets convert traffic into financial value",
            },
            "tools": ["Prospectus", "Business Model", "Financial Analysis", "PPT"],
            "role": "Analyzed industry trends, city traffic, core businesses and profitability quality.",
            "deliverables": ["IPO business analysis deck", "Core asset analysis"],
            "target_roles": ["Consulting", "Investment Research", "Business Analysis"],
            "download_file": "assets/projects/shaanxi_tourism_ipo.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "Holiland Marketing Strategy Plan",
            "category": "Business Research",
            "summary": "A structured marketing plan for Holiland, covering brand rejuvenation, IP collaborations, consumer behavior and 4P strategy.",
            "logic": {
                "Problem": "High-frequency IP collaborations bring traffic but may dilute brand assets",
                "Method": "Combined PEST, SWOT, STP, 4P and consumer behavior analysis",
                "Output": "Created a marketing strategy report and brand improvement suggestions",
                "Value": "Turns brand heat issues into actionable marketing optimization paths",
            },
            "tools": ["PEST", "SWOT", "STP", "4P", "Consumer Analysis"],
            "role": "Analyzed brand background, consumer behavior, competitors and marketing problems.",
            "deliverables": ["Marketing report", "Consumer analysis", "Brand strategy suggestions"],
            "target_roles": ["Marketing", "Consulting", "Business Analysis"],
            "download_file": "assets/projects/holiland_marketing.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "AI + Financial Data Analysis Website",
            "category": "AI x Finance",
            "summary": "A lightweight Streamlit tool that calls LLM APIs to summarize financial text, extract key fields and generate structured outputs.",
            "logic": {
                "Problem": "Finance workflows contain large volumes of unstructured text and repeated reading costs",
                "Method": "Used LLM APIs and prompt constraints for summary, extraction and formatting",
                "Output": "Generated structured results, key summaries and visual display",
                "Value": "Supports human review and makes financial information processing clearer",
            },
            "tools": ["Streamlit", "Python", "LLM API", "Prompt Engineering"],
            "role": "Designed site functions, prompt output format, data cleaning flow and display pages.",
            "deliverables": ["Live demo", "Structured output template", "Project PDF"],
            "target_roles": ["AI Finance", "Business Analysis", "Data Analysis"],
            "download_file": "assets/projects/ai_finance_website.pdf",
            "github_url": "",
            "demo_url": "https://auditflow13.streamlit.app/",
        },
        {
            "name": "Research on AGI Adoption and Corporate Governance",
            "category": "AI x Finance",
            "summary": "A research project studying whether AGI adoption can improve corporate governance through earnings management, disclosure quality, executive pay and related-party transactions.",
            "logic": {
                "Problem": "Can AI or AGI reduce managerial information advantages and improve governance",
                "Method": "Built an AGI keyword dictionary from annual-report MD&A and matched governance variables",
                "Output": "Completed technical route, variable design and panel-regression framework",
                "Value": "Turns AI strategy text into measurable corporate-governance research variables",
            },
            "tools": ["Python", "Text Mining", "Stata", "CSMAR", "Wind"],
            "role": "Supported research framework design, theoretical mechanism, keyword dictionary construction and data processing.",
            "deliverables": ["Project proposal", "Defense deck", "Variable design"],
            "target_roles": ["Research", "AI Business Analysis", "Data Analysis"],
            "download_file": "assets/projects/agi_governance_research.pdf",
            "github_url": "",
            "demo_url": "",
        },
        {
            "name": "City Pizza WeChat Ordering Mini Program",
            "category": "Product & Coding",
            "summary": "An AI-assisted WeChat mini-program prototype covering user ordering flows and merchant-side dish, order, member and report management.",
            "logic": {
                "Problem": "Small restaurants need configurable ordering, product and order-management tools",
                "Method": "Designed the user ordering path and merchant management modules",
                "Output": "Completed mini-program prototype, SKU management and backend page structure",
                "Value": "Shows the ability to move from business process to product prototype with AI-assisted coding",
            },
            "tools": ["WeChat Mini Program", "JavaScript", "WXML", "WXSS", "GitHub"],
            "role": "Designed page structure, business flows, merchant backend modules and product management logic.",
            "deliverables": ["Mini-program prototype", "Merchant backend pages", "GitHub repository"],
            "target_roles": ["Product", "Operations", "AI-assisted Coding"],
            "download_file": "assets/projects/city_pizza_miniprogram.pdf",
            "github_url": "https://github.com/starer1333/CSPS-mini-program",
            "demo_url": "",
        },
    ],
}


CSS = """
<style>
:root {
  --bg-main: #F5F5F7;
  --bg-card: #FFFFFF;
  --bg-soft: #FAFAFA;
  --text-main: #1D1D1F;
  --text-secondary: #6E6E73;
  --text-muted: #86868B;
  --accent-blue: #0071E3;
  --border-light: #E5E5EA;
  --shadow-soft: 0 12px 32px rgba(0, 0, 0, 0.06);
  --shadow-hover: 0 18px 45px rgba(0, 0, 0, 0.10);
}

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg-main);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Segoe UI", sans-serif;
}

[data-testid="stHeader"], [data-testid="stToolbar"], footer {
  display: none;
}

.block-container {
  max-width: 1180px;
  padding: 32px 24px 72px;
}

h1, h2, h3, p {
  letter-spacing: 0;
}

.nav {
  position: sticky;
  top: 0;
  z-index: 999;
  margin: -32px -24px 24px;
  padding: 14px 24px;
  background: rgba(245, 245, 247, 0.86);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.nav-inner {
  max-width: 1180px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.brand {
  font-weight: 700;
  font-size: 16px;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  font-size: 14px;
}

.nav-links a {
  color: var(--text-secondary) !important;
  text-decoration: none;
}

.language-bar {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 22px;
}

.language-card {
  width: min(360px, 100%);
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid var(--border-light);
  border-radius: 18px;
  padding: 10px 14px;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
  gap: 32px;
  align-items: center;
  padding: 24px 0 56px;
}

.eyebrow {
  color: var(--accent-blue);
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 14px;
}

.hero h1 {
  font-size: clamp(48px, 7vw, 72px);
  line-height: 1.02;
  margin: 0 0 18px;
}

.hero-subtitle {
  color: var(--text-secondary);
  font-size: clamp(19px, 2.3vw, 26px);
  line-height: 1.45;
  margin-bottom: 28px;
}

.hero-card, .card, .project-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: 28px;
  box-shadow: var(--shadow-soft);
}

.hero-card {
  padding: 30px;
}

.metric {
  padding: 20px 0;
  border-bottom: 1px solid var(--border-light);
}

.metric:last-child {
  border-bottom: 0;
}

.metric strong {
  display: block;
  font-size: 34px;
  line-height: 1;
}

.metric span {
  color: var(--text-secondary);
  font-size: 14px;
}

.button-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 42px;
  padding: 10px 18px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 650;
  text-decoration: none !important;
  transition: transform 0.2s ease, background 0.2s ease;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn-primary {
  background: var(--accent-blue);
  color: white !important;
}

.btn-secondary {
  background: #ECECF1;
  color: var(--text-main) !important;
}

.section {
  padding: 42px 0;
}

.section h2 {
  font-size: clamp(34px, 4vw, 48px);
  margin: 0 0 14px;
}

.section-lead {
  color: var(--text-secondary);
  font-size: 18px;
  line-height: 1.6;
  max-width: 780px;
  margin-bottom: 28px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.card, .project-card {
  padding: 28px;
}

.project-card {
  margin-bottom: 12px;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-hover);
}

.project-actions {
  margin: -2px 0 26px;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 16px 0;
}

.tag {
  display: inline-flex;
  padding: 7px 11px;
  border-radius: 999px;
  background: var(--bg-soft);
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 600;
}

.tag-blue {
  color: var(--accent-blue);
  background: #F0F7FF;
  border-color: #CFE5FF;
}

.logic {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin: 22px 0;
}

.logic-step {
  background: var(--bg-soft);
  border: 1px solid var(--border-light);
  border-radius: 18px;
  padding: 16px;
  min-height: 120px;
}

.logic-step-title {
  color: var(--accent-blue);
  font-size: 13px;
  font-weight: 750;
  margin-bottom: 8px;
}

.logic-step-content {
  color: var(--text-main);
  font-size: 14px;
  line-height: 1.45;
}

.muted {
  color: var(--text-secondary);
}

.small {
  font-size: 14px;
}

.divider {
  height: 1px;
  background: var(--border-light);
  margin: 28px 0;
}

div[data-testid="stExpander"] {
  border: 1px solid var(--border-light);
  border-radius: 18px;
  background: #fff;
  box-shadow: none;
  margin-bottom: 24px;
}

div[data-testid="stRadio"] label {
  color: var(--text-main);
}

div.stButton > button, div.stDownloadButton > button, a[data-testid="stLinkButton"] {
  border-radius: 999px;
  min-height: 42px;
  font-weight: 650;
}

@media (max-width: 860px) {
  .hero, .grid-3, .logic {
    grid-template-columns: 1fr;
  }
  .nav-inner {
    align-items: flex-start;
    flex-direction: column;
    gap: 10px;
  }
  .nav-links {
    gap: 12px;
  }
  .card, .project-card, .hero-card {
    padding: 22px;
  }
  .language-bar {
    justify-content: stretch;
  }
}
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def get_language() -> str:
    st.markdown('<div class="language-bar"><div class="language-card">', unsafe_allow_html=True)
    lang = st.radio(
        I18N["中文"]["lang_label"],
        ["中文", "English"],
        horizontal=True,
        label_visibility="collapsed",
    )
    st.markdown("</div></div>", unsafe_allow_html=True)
    return lang


def nav(content: dict[str, object]) -> None:
    labels = content["nav"]
    st.markdown(
        f"""
        <div class="nav">
          <div class="nav-inner">
            <div class="brand">Amber Wang</div>
            <div class="nav-links">
              <a href="#home">{labels[0]}</a>
              <a href="#about">{labels[1]}</a>
              <a href="#projects">{labels[2]}</a>
              <a href="#ai-lab">{labels[3]}</a>
              <a href="#resume">{labels[4]}</a>
              <a href="#contact">{labels[5]}</a>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tags(items: list[str], blue_first: bool = False) -> str:
    html = ['<div class="tag-row">']
    for index, item in enumerate(items):
        cls = "tag tag-blue" if blue_first and index == 0 else "tag"
        html.append(f'<span class="{cls}">{item}</span>')
    html.append("</div>")
    return "".join(html)


def logic_map(logic: dict[str, str]) -> str:
    html = ['<div class="logic">']
    for title, body in logic.items():
        html.append(
            f"""
            <div class="logic-step">
              <div class="logic-step-title">{title}</div>
              <div class="logic-step-content">{body}</div>
            </div>
            """
        )
    html.append("</div>")
    return "".join(html)


def section_title(anchor: str, title: str, lead: str) -> None:
    st.markdown(
        f"""
        <div class="section" id="{anchor}">
          <h2>{title}</h2>
          <p class="section-lead">{lead}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_download(path: str, content: dict[str, object], key: str) -> None:
    file_path = BASE_DIR / path
    if file_path.exists():
        with open(file_path, "rb") as file:
            st.download_button(
                content["download_pdf"],
                data=file,
                file_name=file_path.name,
                mime="application/pdf",
                key=key,
            )
    else:
        st.button(content["pdf_missing"], disabled=True, key=key)


def project_card(project: dict[str, object], content: dict[str, object], key_prefix: str) -> None:
    st.markdown(
        f"""
        <div class="project-card">
          {tags([project["category"]], blue_first=True)}
          <h3>{project["name"]}</h3>
          <p class="muted">{project["summary"]}</p>
          {logic_map(project["logic"])}
          {tags(project["tools"])}
        </div>
        """,
        unsafe_allow_html=True,
    )

    button_count = 1 + int(bool(project["github_url"])) + int(bool(project["demo_url"]))
    columns = st.columns(button_count)
    with columns[0]:
        render_download(project["download_file"], content, f"{key_prefix}-download")
    column_index = 1
    if project["github_url"]:
        with columns[column_index]:
            st.link_button(content["view_github"], project["github_url"])
        column_index += 1
    if project["demo_url"]:
        with columns[column_index]:
            st.link_button(content["view_demo"], project["demo_url"])

    with st.expander(content["details"]):
        st.markdown(f"**{content['my_role']}**  \n{project['role']}")
        st.markdown(f"**{content['deliverables']}**  \n{', '.join(project['deliverables'])}")
        st.markdown(f"**{content['target_roles']}**  \n{', '.join(project['target_roles'])}")


def home(content: dict[str, object]) -> None:
    metric_html = "".join(
        f'<div class="metric"><strong>{number}</strong><span>{caption}</span></div>'
        for number, caption in content["metrics"]
    )
    chip_html = tags(content["chips"])
    st.markdown(
        f"""
        <div class="hero" id="home">
          <div>
            <div class="eyebrow">{content["hero_eyebrow"]}</div>
            <h1>{content["hero_title"]}</h1>
            <p class="hero-subtitle">{content["hero_subtitle"]}</p>
            <div class="button-row">
              <a class="btn btn-primary" href="#projects">{content["view_projects"]}</a>
              <a class="btn btn-secondary" href="#resume">{content["download_resume"]}</a>
              <a class="btn btn-secondary" href="https://github.com/starer1333" target="_blank">GitHub</a>
            </div>
            <div style="margin-top: 24px;">{chip_html}</div>
          </div>
          <div class="hero-card">{metric_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def about(content: dict[str, object]) -> None:
    section_title("about", content["about_title"], content["about_lead"])
    cards = []
    for title, body, tools in content["pillars"]:
        cards.append(
            f"""
            <div class="card">
              <h3>{title}</h3>
              <p class="muted">{body}</p>
              {tags(tools)}
            </div>
            """
        )
    st.markdown(f'<div class="grid-3">{"".join(cards)}</div>', unsafe_allow_html=True)


def featured_projects(projects: list[dict[str, object]], content: dict[str, object]) -> None:
    section_title("featured", content["featured_title"], content["featured_lead"])
    for index in [5, 0, 2]:
        project_card(projects[index], content, f"featured-{index}")


def projects_section(projects: list[dict[str, object]], content: dict[str, object]) -> None:
    section_title("projects", content["projects_title"], content["projects_lead"])
    categories = [content["all"]] + sorted({project["category"] for project in projects})
    selected = st.radio(
        content["category_label"],
        categories,
        horizontal=True,
        label_visibility="collapsed",
    )
    visible = projects if selected == content["all"] else [project for project in projects if project["category"] == selected]
    for index, project in enumerate(visible):
        project_card(project, content, f"project-{selected}-{index}")


def ai_lab(content: dict[str, object]) -> None:
    section_title("ai-lab", content["ai_lab_title"], content["ai_lab_lead"])
    columns = st.columns(2)
    for index, (title, body) in enumerate(content["ai_modules"]):
        with columns[index % 2]:
            st.markdown(
                f"""
                <div class="card">
                  <h3>{title}</h3>
                  <p class="muted">{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def resume(content: dict[str, object]) -> None:
    section_title("resume", content["resume_title"], content["resume_lead"])
    resume_path = BASE_DIR / "assets/resume/resume_latest.pdf"
    if resume_path.exists():
        with open(resume_path, "rb") as file:
            st.download_button(
                content["resume_button"],
                data=file,
                file_name="Amber_Wang_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.info(content["resume_missing"])

    cards = []
    for title, body in content["resume_cards"]:
        cards.append(f'<div class="card"><h3>{title}</h3><p class="muted">{body}</p></div>')
    st.markdown(f'<div class="grid-3">{"".join(cards)}</div>', unsafe_allow_html=True)


def contact(content: dict[str, object]) -> None:
    section_title("contact", content["contact_title"], content["contact_lead"])
    st.markdown(
        f"""
        <div class="card">
          <div class="button-row">
            <a class="btn btn-primary" href="mailto:wangdacongming@icloud.com">Email</a>
            <a class="btn btn-secondary" href="https://github.com/starer1333" target="_blank">GitHub</a>
            <a class="btn btn-secondary" href="https://auditflow13.streamlit.app/" target="_blank">Streamlit Demo</a>
          </div>
          <div class="divider"></div>
          <p class="muted small">{content["footer"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_css()
    lang = get_language()
    content = I18N[lang]
    projects = PROJECTS[lang]
    nav(content)
    home(content)
    about(content)
    featured_projects(projects, content)
    projects_section(projects, content)
    ai_lab(content)
    resume(content)
    contact(content)


if __name__ == "__main__":
    main()
