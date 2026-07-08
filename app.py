import os
from html import escape
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
        "chips": ["Audit & Accounting", "Business Research", "AI × Finance", "AI × Healthcare", "People Operations"],
        "metrics": [
            ("10", "覆盖审计、商业研究、AI、医疗健康和产品原型的作品集项目"),
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
        "resume_lead": "你可以按投递方向下载对应版本简历。每份 PDF 都包含中文与英文版本，顺序为中文在前、英文在后。",
        "resume_missing": "简历文件暂未上传。",
        "resume_cards": [
            ("审计 / 会计方向", "Audit workflow · Excel automation · Financial data", "王渤函-会计.pdf", "下载会计简历"),
            ("行业研究 / 咨询方向", "Industry research · Strategy deck · Financial analysis", "王渤函-行研.pdf", "下载行研简历"),
            ("HR / People Operations", "People operations · HR analytics · Business communication", "王渤函-HR.pdf", "下载 HR 简历"),
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
        "chips": ["Audit & Accounting", "Business Research", "AI × Finance", "AI × Healthcare", "People Operations"],
        "metrics": [
            ("10", "Portfolio projects across audit, research, AI, healthcare and product"),
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
                "Audit workflows, financial data processing and documentation logic are organized into clear, repeatable processes.",
                ["Audit", "Excel", "VBA"],
            ),
            (
                "Business Research Thinking",
                "Industry, company, business model and financial analysis are structured into consulting-style conclusions.",
                ["Research", "Strategy", "PPT"],
            ),
            (
                "AI-enabled Workflow Builder",
                "AI-assisted coding, LLM APIs and knowledge-base tools are used to process unstructured business materials.",
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
        "resume_lead": "Download the resume version that best matches the role. Each PDF includes both Chinese and English versions, with Chinese first and English second.",
        "resume_missing": "Resume file pending.",
        "resume_cards": [
            ("Audit / Accounting", "Audit workflow · Excel automation · Financial data", "王渤函-会计.pdf", "Download Accounting Resume"),
            ("Business Research / Consulting", "Industry research · Strategy deck · Financial analysis", "王渤函-行研.pdf", "Download Research Resume"),
            ("HR / People Operations", "People operations · HR analytics · Business communication", "王渤函-HR.pdf", "Download HR Resume"),
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


DOWNLOAD_FILES = {
    "ai_finance_bp": "assets/projects/AI 财务BP 2028.pdf",
    "ipo_earnings_pdf": "assets/projects/会计师事务所审计供给能力对IPO企业应计盈余管理的影响研究.pdf",
    "ipo_earnings_do": "assets/projects/会计师事务所审计供给能力对IPO企业应计盈余管理的影响研究.do",
    "longi_internal_control_pptx": "assets/projects/长飞光纤 内部控制分析.pptx",
    "holiland": "assets/projects/好利来营销策划案.pdf",
    "agi_governance_pdf": "assets/projects/AGI引入对公司治理效果的影响研究.pdf",
    "agi_defense_pdf": "assets/projects/论文答辩 .pdf",
    "shaanxi_tourism": "assets/projects/陕西文旅公司分析.pptx",
    "volkswagen": "assets/projects/大众汽车集团行业研究.pdf",
    "baidu_health": "assets/projects/百度健康行业研究框架与战略分析.pdf",
}


PROJECT_LINKS = {
    "personal_website": "https://github.com/starer1333/amber-personal-website",
    "city_pizza": "https://github.com/starer1333/CSPS-mini-program",
    "financedoc_ai_github": "https://github.com/starer1333/financedoc-ai",
    "financedoc_ai_demo": "https://financedoc-ai.streamlit.app/",
    "auditflow_demo": "https://auditflow13.streamlit.app/",
}


CATEGORIES = {
    "中文": ["全部", "Audit & Accounting", "Business Research & Consulting", "AI × Finance", "AI × Healthcare", "Product & Coding", "People Operations"],
    "English": ["All", "Audit & Accounting", "Business Research & Consulting", "AI × Finance", "AI × Healthcare", "Product & Coding", "People Operations"],
}


PROJECTS = {
    "中文": [
        {
            "id": "audit_confirmation",
            "name": "审计函证流程与 AI 辅助数据处理",
            "category": "Audit & Accounting",
            "tags": ["审计流程", "Excel", "VBA", "DeepSeek", "Dify"],
            "summary": "在天职国际函证中心实习期间，我参与 30+ 企业函证流程管理，覆盖发函、跟踪、回函核验和异常处理，并使用 Excel、VBA 与 AI 工具优化重复性数据处理流程。",
            "logic": {
                "Problem": "函证流程存在大量重复数据整理、状态跟踪和异常核验工作",
                "Method": "用 Excel 高级函数、数据透视表、VBA 与 AI 工具辅助流程处理",
                "Output": "形成进度统计、自动化提取模板、批量重命名脚本和知识库探索",
                "Value": "提升函证流程透明度，支持项目经理更快定位异常事项",
            },
            "details": [
                "**函证流程全周期管理：** 独立负责 30+ 家企业函证流程，跟进发函、回函核验、异常处理和项目进度更新，协助保证函证流程闭环。",
                "**数据整理与效率优化：** 使用 VLOOKUP、XLOOKUP、COUNTIF、数据透视表等工具批量处理函证数据，并设计自动化提取模板。",
                "**AI 辅助自动化实践：** 使用 DeepSeek 辅助编写 VBA 脚本，实现文件批量重命名、数据清洗和异常标注，减少重复性手工处理。",
                "**业务规则结构化：** 将函证核验、资金流水备注、异常情况处理等业务规则转化为可被 AI 理解的指令和判断逻辑。",
                "**智能化工具探索：** 参与 Dify 函证知识库、RPA 与 OCR 应用测试，理解 AI 在审计流程中的辅助价值。",
            ],
            "tools": ["Excel", "VBA", "DeepSeek", "Dify", "RPA/OCR"],
            "deliverables": ["脱敏流程总结", "函证进度统计", "自动化处理模板"],
            "target_roles": ["审计", "会计", "财务共享", "审计数据分析"],
            "downloads": [],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "ipo_earnings",
            "name": "IPO 企业盈余管理研究",
            "category": "Audit & Accounting",
            "tags": ["审计研究", "IPO", "Stata", "修正 Jones 模型"],
            "summary": "基于 2011-2024 年 A 股 IPO 公司样本，研究审计师行业专长是否能够抑制 IPO 企业应计盈余管理。",
            "logic": {
                "Problem": "IPO 企业可能存在美化上市业绩和应计盈余管理动机",
                "Method": "使用修正 Jones 模型测度 AbsDA，并构建审计师行业专长变量",
                "Output": "完成固定效应回归、工具变量、机制分析和论文写作",
                "Value": "解释审计供给能力对 IPO 盈余质量的治理作用",
            },
            "details": [
                "**研究问题界定：** 聚焦 IPO 企业在上市前后可能存在的应计盈余管理行为，分析审计供给能力的治理作用。",
                "**变量设计：** 使用审计师行业专长衡量事务所审计供给能力，并用修正 Jones 模型测度应计盈余管理程度。",
                "**模型构建：** 构建包含年度固定效应的面板回归模型，检验行业专长与应计盈余管理之间的关系。",
                "**稳健性与内生性处理：** 使用同行业同年度行业专长均值作为工具变量，缓解潜在内生性问题。",
                "**机制分析：** 进一步讨论事务所规模和审计收费在行业专长影响盈余管理过程中的作用。",
            ],
            "tools": ["CSMAR", "Stata", "Modified Jones", "Fixed Effects", "IV"],
            "deliverables": ["研究论文", "变量定义表", "Stata do 文件"],
            "target_roles": ["审计", "会计研究", "数据分析"],
            "downloads": [
                {"label": "下载论文 PDF", "path": DOWNLOAD_FILES["ipo_earnings_pdf"]},
                {"label": "下载 Stata do 文件", "path": DOWNLOAD_FILES["ipo_earnings_do"]},
            ],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "volkswagen_strategy",
            "name": "大众汽车集团行业研究与战略财务分析",
            "category": "Business Research & Consulting",
            "tags": ["汽车行业", "战略分析", "财务分析", "咨询式 Deck"],
            "summary": "以大众汽车集团为对象，分析收入横盘、利润率下滑、中国市场压力和软件转型瓶颈，形成咨询式战略财务分析演示文稿。",
            "logic": {
                "Problem": "传统车企在电动化和软件定义汽车时代面临利润质量修复压力",
                "Method": "拆解行业价值池迁移、财务表现、竞争格局和软件平台瓶颈",
                "Output": "形成战略财务分析 deck、核心结论页和利润率修复建议",
                "Value": "把复杂行业变化转化为可讨论的战略财务判断",
            },
            "details": [
                "**行业趋势判断：** 从电动化、软件定义汽车、AI 出行和中国市场竞争角度分析汽车行业价值池迁移。",
                "**财务问题拆解：** 对大众收入、营业利润率、净利润、现金流和 ROE 进行拆解，判断利润质量压力来源。",
                "**竞争格局分析：** 对比丰田、特斯拉、比亚迪及中国车企，识别大众面临的效率、软件和成本压力。",
                "**战略瓶颈诊断：** 分析 CARIAD、软件平台、电子电气架构和中国市场产品定义问题。",
                "**咨询式表达：** 将分析结果整理为高信息密度 deck，形成核心结论、利润桥、战略建议和风险提示。",
            ],
            "tools": ["Annual Report", "Profit Bridge", "DuPont", "Competition Analysis", "PPT"],
            "deliverables": ["战略财务分析 PDF", "核心结论页", "利润率修复建议"],
            "target_roles": ["行业研究", "咨询", "战略分析", "商业分析"],
            "downloads": [{"label": "下载项目 PDF", "path": DOWNLOAD_FILES["volkswagen"]}],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "shaanxi_tourism",
            "name": "陕西文旅 IPO 商业分析",
            "category": "Business Research & Consulting",
            "tags": ["IPO", "文旅行业", "商业模式", "财务分析"],
            "summary": "围绕陕西旅游文化产业股份有限公司 IPO，分析文旅行业增长、核心资产壁垒、演艺 + 索道业务模型和盈利质量。",
            "logic": {
                "Problem": "如何判断一家文旅公司的 IPO 投资价值和商业壁垒",
                "Method": "拆解行业增长、西安流量、文化 IP、演艺与索道核心业务",
                "Output": "形成 IPO 商业分析 deck、核心资产分析和盈利质量判断",
                "Value": "帮助快速理解文旅资产的流量转化和资本市场叙事",
            },
            "details": [
                "**行业增长逻辑分析：** 从国内旅游人次、文旅消费升级和体验式旅游趋势判断行业增长基础。",
                "**核心资产识别：** 分析西安文化 IP、华清宫《长恨歌》和华山西峰索道等资源型资产的稀缺性。",
                "**商业模式拆解：** 将公司业务拆解为演艺、索道和其他业务，判断收入结构和流量转化能力。",
                "**盈利质量判断：** 结合净利率、现金流和核心业务占比，分析公司盈利能力的可持续性。",
                "**资本市场叙事：** 将行业、资产、业务和财务逻辑整合成 IPO 路演式分析框架。",
            ],
            "tools": ["Prospectus", "Business Model", "Financial Analysis", "PPT"],
            "deliverables": ["IPO 商业分析 deck", "核心资产分析", "盈利质量判断"],
            "target_roles": ["咨询", "投研", "商业分析"],
            "downloads": [{"label": "下载项目 PPTX", "path": DOWNLOAD_FILES["shaanxi_tourism"]}],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "holiland_marketing",
            "name": "好利来营销策划案",
            "category": "Business Research & Consulting",
            "tags": ["营销策略", "消费者行为", "4P", "品牌分析"],
            "summary": "以好利来为研究对象，围绕品牌年轻化、IP 联名、消费者行为和 4P 策略进行系统分析。",
            "logic": {
                "Problem": "高频 IP 联名带来流量，也可能造成审美疲劳和品牌资产弱化",
                "Method": "结合 PEST、SWOT、STP、4P 和消费者行为分析",
                "Output": "形成营销策划报告、消费者分析和品牌策略建议",
                "Value": "把品牌热度问题转化为可落地的营销优化路径",
            },
            "details": [
                "**品牌与业务梳理：** 分析好利来发展阶段、核心产品系列、直营门店模式和多品牌矩阵。",
                "**市场环境分析：** 使用 PEST、SWOT 和竞品分析框架，判断烘焙行业竞争和消费升级趋势。",
                "**消费者行为研究：** 从消费者画像、购买动机、6W1H 和 Z 世代情绪价值角度分析目标客群。",
                "**问题诊断：** 识别高频 IP 联名、健康化转型滞后、IP 依赖和定价争议等品牌问题。",
                "**策略建议输出：** 基于 4P 框架提出产品、价格、渠道和促销优化建议。",
            ],
            "tools": ["PEST", "SWOT", "STP", "4P", "Consumer Analysis"],
            "deliverables": ["营销策划报告", "消费者分析", "品牌策略建议"],
            "target_roles": ["市场", "咨询", "商业分析"],
            "downloads": [{"label": "下载报告 PDF", "path": DOWNLOAD_FILES["holiland"]}],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "financedoc_ai",
            "name": "FinanceDoc AI｜财务文档智能分析与风险审阅系统",
            "category": "AI × Finance",
            "tags": ["Streamlit", "DeepSeek API", "RAG", "Multi-Agent", "财务分析", "风险审阅"],
            "summary": "基于 Streamlit 搭建财务文档智能分析系统，支持文档上传、表格解析、财务摘要、风险识别、RAG 问答、多 Agent 审阅和底稿导出。",
            "logic": {
                "Problem": "财务文档、审计报告和尽调材料信息密度高，人工初筛耗时",
                "Method": "使用 Streamlit + DeepSeek API + RAG + 规则识别构建分析流程",
                "Output": "生成财务摘要、风险审阅、问答证据片段和分析底稿",
                "Value": "将财务数据录入、风险审阅和底稿生成流程产品化",
            },
            "details": [
                "**系统工作流设计：** 将项目拆解为项目概览、数据输入、财务摘要、风险审阅、RAG 问答、Multi-Agent 分析和底稿导出七个模块。",
                "**多格式文档解析：** 支持上传 PDF、Excel、CSV 文件，并通过 PyPDF2、pandas、openpyxl 提取文本和表格信息。",
                "**关键指标识别：** 自动识别收入、成本、利润、现金流、资产负债等关键字段，并生成财务摘要和趋势图表。",
                "**风险审阅设计：** 基于规则识别收入下降、利润承压、现金流质量、负债率、费用率、审计意见和关联交易等风险。",
                "**RAG 与 Multi-Agent：** 接入 DeepSeek API，结合 RAG 检索和多角色 Agent 完成审阅。",
                "**底稿导出：** 支持导出 Markdown、CSV、Word 和 PDF 审计底稿，使项目更接近真实财务分析 / 审计辅助工具。",
            ],
            "tools": ["Python", "Streamlit", "Pandas", "Plotly", "PyPDF2", "openpyxl", "DeepSeek API", "RAG", "Multi-Agent"],
            "deliverables": ["在线 Demo", "GitHub 仓库", "财务摘要", "风险审阅结果", "分析底稿导出"],
            "target_roles": ["AI 财务", "审计数据分析", "财务分析", "商业分析", "AI 产品助理"],
            "downloads": [],
            "github_url": PROJECT_LINKS["financedoc_ai_github"],
            "demo_url": PROJECT_LINKS["financedoc_ai_demo"],
            "image_file": "",
        },
        {
            "id": "agi_governance",
            "name": "AGI 引入对公司治理效果的影响研究",
            "category": "AI × Finance",
            "tags": ["AGI", "公司治理", "文本挖掘", "面板回归"],
            "summary": "研究 AGI 引入是否能够改善上市公司治理效果，关注盈余管理、信息披露质量、高管薪酬和关联交易等治理维度。",
            "logic": {
                "Problem": "AI / AGI 是否能缓解管理层信息优势并改善公司治理",
                "Method": "基于年报 MD&A 文本构建 AGI 关键词词典并匹配治理变量",
                "Output": "完成技术路线、变量设计、面板回归框架和答辩材料",
                "Value": "把 AI 战略文本转化为可检验的公司治理研究变量",
            },
            "details": [
                "**研究框架设计：** 围绕 AGI、信息不对称和公司治理效果之间的关系，参与理论机制推导和研究假设设计。",
                "**关键词词典构建：** 基于 AGI 与智能体相关理论文献，构建年报 MD&A 文本扫描所需的关键词词典。",
                "**文本数据处理：** 使用 Python 对 A 股上市公司年报文本进行关键词匹配和词频统计，构建企业层面的 AGI 引入指标。",
                "**实证数据整理：** 使用 Excel / Stata 整合 CSMAR、Wind、CNRDS 等数据库变量，完成多表匹配和样本清洗。",
                "**模型与结果分析：** 参与面板回归、调节效应和稳健性检验，用于分析 AGI 对公司治理变量的影响。",
            ],
            "tools": ["Python", "Text Mining", "Stata", "CSMAR", "Wind", "CNRDS"],
            "deliverables": ["项目申请书", "答辩材料", "变量设计", "技术路线图"],
            "target_roles": ["学术研究", "AI 商业分析", "数据分析"],
            "downloads": [
                {"label": "下载项目申请书", "path": DOWNLOAD_FILES["agi_governance_pdf"]},
                {"label": "下载答辩材料", "path": DOWNLOAD_FILES["agi_defense_pdf"]},
            ],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "city_pizza",
            "name": "City Pizza 微信点餐小程序",
            "category": "Product & Coding",
            "tags": ["微信小程序", "产品原型", "AI-assisted Coding", "商家后台"],
            "summary": "使用 AI 辅助开发微信点餐小程序原型，包含用户端点餐流程和商家端后台管理模块。",
            "logic": {
                "Problem": "小型餐饮门店需要可配置的点餐、商品和订单管理工具",
                "Method": "设计用户点餐路径、商品规格逻辑和商家后台管理模块",
                "Output": "完成小程序原型、商家后台页面和 GitHub 仓库沉淀",
                "Value": "展示从业务流程到产品原型的 AI-assisted coding 能力",
            },
            "details": [
                "**需求拆解：** 将餐饮门店需求拆解为用户点餐、购物车、订单提交、会员体系和商家后台管理模块。",
                "**页面结构设计：** 设计首页、点餐、订单、我的四个用户端 Tab，并补充商家端 dashboard、菜品、分类、订单、会员、优惠券、报表等页面。",
                "**商品管理逻辑：** 实现菜品名称、详细介绍、分类、价格、图片 URL、排序和上架状态等字段管理。",
                "**规格与加料管理：** 支持单选 / 多选规格组、规格项名称、价格、编辑和删除，用于模拟餐饮商品配置场景。",
                "**GitHub 项目沉淀：** 将小程序代码上传到 GitHub，作为 AI-assisted coding 和产品原型落地能力的证明。",
            ],
            "tools": ["WeChat Mini Program", "JavaScript", "WXML", "WXSS", "GitHub"],
            "deliverables": ["小程序原型", "商家后台页面", "GitHub 仓库"],
            "target_roles": ["产品", "运营", "AI-assisted Coding"],
            "downloads": [],
            "github_url": PROJECT_LINKS["city_pizza"],
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "baidu_health_strategy",
            "name": "百度健康行业研究框架与战略分析",
            "category": "Business Research & Consulting",
            "tags": ["行业研究", "互联网医疗", "AI × Healthcare", "商业模式分析", "战略分析"],
            "summary": "围绕百度健康在中国数字健康与互联网医疗行业中的平台机会展开研究，分析其行业政策、商业模式、竞争格局、财务压力和战略定位。",
            "logic": {
                "Problem": "百度健康不适合简单复制京东健康的重履约医药零售模式",
                "Method": "从行业政策、商业模式、竞争对标、财务经营和国际案例四个维度展开分析",
                "Output": "形成百度健康的平台定位、业务边界、变现路径和战略建议",
                "Value": "帮助判断百度健康如何借助 AI 搜索、知识图谱和患者服务编排形成差异化竞争",
            },
            "details": [
                "**研究边界界定：** 将百度健康定位为中国数字健康行业中的“平台层”机会，重点分析其在流量入口、医疗信息组织、患者服务和医院/医生连接中的角色。",
                "**行业与政策分析：** 梳理中国数字健康、互联网医疗、AI 医疗卫生和分级诊疗政策，判断百度健康更适合切入智能预问诊、分诊导诊、慢病管理和院后随访等流程型场景。",
                "**商业模式拆解：** 区分百度健康与京东健康的能力曲线，指出百度优势在搜索流量、AI 能力、知识图谱和开放平台生态，而非药品供应链和交易履约。",
                "**竞争对标分析：** 对比百度健康与京东健康、阿里健康及国际互联网健康业务案例，判断哪些模式可以迁移到中国市场，哪些模式存在监管与履约边界。",
                "**信息边界说明：** 百度未单独披露百度健康收入、利润、MAU、付费转化和 GMV，因此不将其单独财务规模伪造成已验证事实。",
                "**战略建议输出：** 提出百度健康应围绕 AI 搜索入口、可信健康内容、医生/医院数字化工具、患者服务编排和 B2B2C 平台模式构建轻资产健康业务。",
            ],
            "tools": ["行业研究", "商业模式分析", "竞争对标", "财务分析", "战略框架", "政策分析"],
            "deliverables": ["行业研究报告", "战略分析框架", "竞争对标结论", "平台定位建议"],
            "target_roles": ["行业研究", "咨询", "战略分析", "互联网医疗", "AI 产品助理", "商业分析"],
            "downloads": [{"label": "下载研究报告", "path": DOWNLOAD_FILES["baidu_health"]}],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
        {
            "id": "fiberhome_internal_control",
            "name": "长飞光纤内部控制分析",
            "category": "Audit & Accounting",
            "tags": ["内部控制", "财务分析", "审计", "PPT"],
            "summary": "围绕长飞光纤的内部控制体系、业务流程和财务风险展开分析，形成内部控制分析报告和展示材料。",
            "logic": {
                "Problem": "制造业企业业务流程复杂，内部控制有效性会影响财务质量与经营风险",
                "Method": "结合内部控制框架、财务指标和业务流程进行风险识别",
                "Output": "形成内部控制分析展示材料与风险识别结论",
                "Value": "展示会计审计基础、流程分析和风险识别能力",
            },
            "details": [
                "**控制环境梳理：** 从公司治理、组织结构和业务流程角度理解内部控制基础。",
                "**风险点识别：** 结合采购、生产、销售、资金和存货等环节识别潜在控制风险。",
                "**财务指标辅助判断：** 使用财务数据观察经营效率、偿债压力和现金流质量。",
                "**报告表达：** 将分析过程整理为 PDF 与 PPTX，便于审计 / 会计岗位展示。",
            ],
            "tools": ["Internal Control", "Financial Analysis", "Excel", "PPT"],
            "deliverables": ["内部控制分析展示材料", "风险识别结论"],
            "target_roles": ["审计", "会计", "内控", "风险管理"],
            "downloads": [
                {"label": "下载 PPTX", "path": DOWNLOAD_FILES["longi_internal_control_pptx"]},
            ],
            "github_url": "",
            "demo_url": "",
            "image_file": "",
        },
    ],
}


PROJECTS["English"] = PROJECTS["中文"]


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
  --accent-teal: #0A7C78;
  --accent-gold: #B8860B;
  --accent-rose: #A23E48;
  --accent-ink: #243447;
  --border-light: #E5E5EA;
  --shadow-soft: 0 14px 34px rgba(36, 52, 71, 0.07);
  --shadow-hover: 0 20px 52px rgba(36, 52, 71, 0.12);
}

html, body, [data-testid="stAppViewContainer"] {
  background:
    linear-gradient(180deg, #F7F8FB 0%, #F5F5F7 42%, #F1F4F3 100%);
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
  grid-template-columns: minmax(0, 1fr) minmax(260px, 340px);
  gap: 28px;
  align-items: center;
  padding: 24px 0 56px;
  overflow: hidden;
}

.eyebrow {
  color: var(--accent-blue);
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 14px;
}

.hero h1 {
  font-size: clamp(42px, 6vw, 64px);
  line-height: 1.02;
  margin: 0 0 18px;
  max-width: 100%;
}

.hero-subtitle {
  color: var(--text-secondary);
  font-size: clamp(18px, 2vw, 23px);
  line-height: 1.45;
  margin-bottom: 28px;
  max-width: 820px;
}

.hero-card, .card, .project-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: 28px;
  box-shadow: var(--shadow-soft);
}

.hero-card {
  padding: 30px;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.96), rgba(248, 251, 250, 0.96)),
    linear-gradient(90deg, rgba(0, 113, 227, 0.08), rgba(184, 134, 11, 0.10));
  border-color: rgba(10, 124, 120, 0.16);
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

.card p {
  margin: 14px 0 0;
  text-align: left;
  line-height: 1.55;
}

.project-card {
  position: relative;
  overflow: hidden;
  margin-bottom: 12px;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.project-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-teal), var(--accent-gold));
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
  align-items: center;
  justify-content: center;
  padding: 7px 11px;
  border-radius: 999px;
  background: var(--bg-soft);
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 600;
  line-height: 1.2;
  white-space: nowrap;
}

.tag-blue {
  color: var(--accent-blue);
  background: #F0F7FF;
  border-color: #CFE5FF;
}

.logic {
  display: grid;
  grid-template-columns: repeat(4, minmax(180px, 1fr));
  gap: 12px;
  margin: 22px 0;
}

.logic-step {
  overflow: hidden;
  background: linear-gradient(180deg, #FFFFFF 0%, #FAFBFC 100%);
  border: 1px solid var(--border-light);
  border-radius: 18px;
  padding: 16px;
  min-height: 132px;
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
  overflow-wrap: anywhere;
  word-break: normal;
  white-space: normal;
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

@media (max-width: 1100px) {
  .hero {
    grid-template-columns: 1fr;
  }

  .hero-card {
    max-width: 520px;
  }
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


def html_block(markup: str) -> None:
    if hasattr(st, "html"):
        st.html(markup)
    else:
        st.markdown(markup, unsafe_allow_html=True)


def get_language() -> str:
    html_block('<div class="language-bar"><div class="language-card">')
    lang = st.radio(
        I18N["中文"]["lang_label"],
        ["中文", "English"],
        horizontal=True,
        label_visibility="collapsed",
    )
    html_block("</div></div>")
    return lang


def nav(content: dict[str, object]) -> None:
    labels = content["nav"]
    html_block(
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
    )


def tags(items: list[str], blue_first: bool = False) -> str:
    html = ['<div class="tag-row">']
    for index, item in enumerate(items):
        cls = "tag tag-blue" if blue_first and index == 0 else "tag"
        html.append(f'<span class="{cls}">{escape(str(item))}</span>')
    html.append("</div>")
    return "".join(html)


def logic_map(logic: dict[str, str]) -> str:
    html = ['<div class="logic">']
    for title, body in logic.items():
        html.append('<div class="logic-step">')
        html.append(f'<div class="logic-step-title">{escape(str(title))}</div>')
        html.append(f'<div class="logic-step-content">{escape(str(body))}</div>')
        html.append("</div>")
    html.append("</div>")
    return "".join(html)


def section_title(anchor: str, title: str, lead: str) -> None:
    html_block(
        f'<div class="section" id="{escape(anchor)}"><h2>{escape(str(title))}</h2><p class="section-lead">{escape(str(lead))}</p></div>',
    )


def get_mime_type(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return "application/pdf"
    if ext == ".pptx":
        return "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    if ext == ".docx":
        return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    if ext == ".do":
        return "text/plain"
    if ext == ".csv":
        return "text/csv"
    return "application/octet-stream"


def render_download_button(label: str, path: str, key: str) -> None:
    if not path:
        return
    file_path = BASE_DIR / path
    if file_path.exists():
        with open(file_path, "rb") as file:
            st.download_button(
                label,
                data=file,
                file_name=file_path.name,
                mime=get_mime_type(str(file_path)),
                key=key,
            )
    else:
        st.warning(f"文件未找到：{path}")


def render_resume_button(label: str, filename: str, key: str) -> None:
    file_path = BASE_DIR / "assets" / "resume" / filename
    if file_path.exists():
        with open(file_path, "rb") as file:
            st.download_button(
                label,
                data=file,
                file_name=file_path.name,
                mime="application/pdf",
                key=key,
            )
    else:
        st.button(label, disabled=True, key=key)


def project_matches_category(project: dict[str, object], selected: str, all_label: str) -> bool:
    if selected == all_label:
        return True
    if project.get("category") == selected:
        return True
    return selected in project.get("tags", [])


def project_card(project: dict[str, object], content: dict[str, object], key_prefix: str) -> None:
    card_html = (
        '<div class="project-card">'
        f'{tags([project["category"]], blue_first=True)}'
        f'<h3>{escape(str(project["name"]))}</h3>'
        f'<p class="muted">{escape(str(project["summary"]))}</p>'
        f'{logic_map(project["logic"])}'
        f'{tags(project["tools"])}'
        '</div>'
    )
    html_block(
        card_html,
    )

    actions = []
    for item_index, item in enumerate(project.get("downloads", [])):
        actions.append(("download", item, f"{key_prefix}-download-{item_index}"))
    if project.get("github_url"):
        actions.append(("github", project["github_url"], f"{key_prefix}-github"))
    if project.get("demo_url"):
        actions.append(("demo", project["demo_url"], f"{key_prefix}-demo"))

    if actions:
        columns = st.columns(len(actions))
        for action_index, (action_type, payload, action_key) in enumerate(actions):
            with columns[action_index]:
                if action_type == "download":
                    render_download_button(str(payload["label"]), str(payload["path"]), action_key)
                elif action_type == "github":
                    st.link_button(content["view_github"], payload)
                elif action_type == "demo":
                    st.link_button(content["view_demo"], payload)

    with st.expander(content["details"]):
        st.markdown(f"**{content['my_role']}**")
        for item in project.get("details", []):
            st.markdown(f"- {item}")
        st.markdown(f"**{content['deliverables']}**  \n{', '.join(project['deliverables'])}")
        st.markdown(f"**{content['target_roles']}**  \n{', '.join(project['target_roles'])}")


def home(content: dict[str, object]) -> None:
    metric_html = "".join(
        f'<div class="metric"><strong>{escape(str(number))}</strong><span>{escape(str(caption))}</span></div>'
        for number, caption in content["metrics"]
    )
    chip_html = tags(content["chips"])
    html_block(
        f"""
        <div class="hero" id="home">
          <div>
            <div class="eyebrow">{escape(str(content["hero_eyebrow"]))}</div>
            <h1>{escape(str(content["hero_title"]))}</h1>
            <p class="hero-subtitle">{escape(str(content["hero_subtitle"]))}</p>
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
    )


def about(content: dict[str, object]) -> None:
    section_title("about", content["about_title"], content["about_lead"])
    cards = []
    for title, body, tools in content["pillars"]:
        cards.append(
            f'<div class="card"><h3>{escape(str(title))}</h3><p class="muted">{escape(str(body))}</p>{tags(tools)}</div>'
        )
    html_block(f'<div class="grid-3">{"".join(cards)}</div>')


def featured_projects(projects: list[dict[str, object]], content: dict[str, object]) -> None:
    section_title("featured", content["featured_title"], content["featured_lead"])
    for index in [5, 0, 2]:
        project_card(projects[index], content, f"featured-{index}")


def projects_section(projects: list[dict[str, object]], content: dict[str, object]) -> None:
    section_title("projects", content["projects_title"], content["projects_lead"])
    categories = CATEGORIES["中文" if content["all"] == "全部" else "English"]
    selected = st.radio(
        content["category_label"],
        categories,
        horizontal=True,
        label_visibility="collapsed",
    )
    visible = [project for project in projects if project_matches_category(project, selected, content["all"])]
    for index, project in enumerate(visible):
        project_card(project, content, f"project-{selected}-{index}")


def ai_lab(content: dict[str, object]) -> None:
    section_title("ai-lab", content["ai_lab_title"], content["ai_lab_lead"])
    columns = st.columns(2)
    for index, (title, body) in enumerate(content["ai_modules"]):
        with columns[index % 2]:
            html_block(
                f"""
                <div class="card">
                  <h3>{title}</h3>
                  <p class="muted">{body}</p>
                </div>
                """,
            )


def resume(content: dict[str, object]) -> None:
    section_title("resume", content["resume_title"], content["resume_lead"])
    columns = st.columns(3)
    for index, (title, body, filename, button_label) in enumerate(content["resume_cards"]):
        with columns[index]:
            html_block(f'<div class="card"><h3>{escape(str(title))}</h3><p class="muted">{escape(str(body))}</p></div>')
            render_resume_button(str(button_label), str(filename), f"resume-{index}")


def contact(content: dict[str, object]) -> None:
    section_title("contact", content["contact_title"], content["contact_lead"])
    html_block(
        f"""
        <div class="card">
          <div class="button-row">
            <a class="btn btn-primary" href="mailto:wangbh2923@mails.jlu.edu.cn">Email</a>
            <a class="btn btn-secondary" href="https://github.com/starer1333" target="_blank">GitHub</a>
            <a class="btn btn-secondary" href="https://financedoc-ai.streamlit.app/" target="_blank">FinanceDoc Demo</a>
          </div>
          <div class="divider"></div>
          <p class="muted small">{content["footer"]}</p>
        </div>
        """,
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
