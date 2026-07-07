# Amber Wang 个人作品集网站

这是一个基于 Streamlit 搭建的个人求职作品集网站，用于展示 Amber Wang 的个人定位、项目作品、AI 工具探索、最新版简历和联系方式。

网站主线是：

- 会计与审计基础
- 商业分析与行业研究能力
- AI x 财务 / AI x 业务工作流能力
- 项目型表达与可展示成果

## 核心功能

- Apple-inspired 的浅色高级作品集 UI
- 中文 / English 双语切换
- Home、About、Projects、AI Lab、Resume、Contact 页面结构
- 项目分类筛选
- 每个项目都有四步逻辑图：Problem -> Method -> Output -> Value
- 支持简历 PDF 和项目 PDF 下载
- 支持 GitHub / Demo 外部链接

## 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud 部署设置

如果网站打不开，请在 Streamlit Cloud 检查这三项：

```text
Repository: starer1333/amber-personal-website
Branch: main
Main file path: app.py
```

如果页面显示构建失败，请先在 Streamlit Cloud 里点击 reboot / redeploy。代码已包含 `requirements.txt`，云端会自动安装 Streamlit。

## 资源文件路径

最新版简历放这里：

```text
assets/resume/resume_latest.pdf
```

项目 PDF 放这里：

```text
assets/projects/
```

如果 PDF 还没有放进去，网站会先显示“PDF 待补充 / PDF pending”。

---

# Amber Wang Portfolio Website

This is a Streamlit-based career portfolio website for Amber Wang. It presents her positioning, project portfolio, AI tool experiments, latest resume and contact information.

The core career story is:

- Accounting and audit foundation
- Business analysis and industry research capability
- AI x finance / AI x business workflow capability
- Project-based communication with portfolio-ready outputs

## Features

- Apple-inspired premium light-mode portfolio UI
- Chinese / English language switch
- Home, About, Projects, AI Lab, Resume and Contact sections
- Filterable project gallery
- Four-step logic map for every project: Problem -> Method -> Output -> Value
- Resume and project PDF download support
- GitHub / Demo external links

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud Deployment

If the website does not open, check these settings in Streamlit Cloud:

```text
Repository: starer1333/amber-personal-website
Branch: main
Main file path: app.py
```

If the page shows a build failure, click reboot / redeploy in Streamlit Cloud. The repo includes `requirements.txt`, so Streamlit Cloud will install Streamlit automatically.

## Asset Paths

Put the latest resume here:

```text
assets/resume/resume_latest.pdf
```

Put project PDFs here:

```text
assets/projects/
```

If PDFs are not added yet, the website will show “PDF 待补充 / PDF pending”.
