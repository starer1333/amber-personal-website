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

## 如何上传 PDF 到网站

最简单的方法是直接在 GitHub 网页上传：

1. 打开仓库：`https://github.com/starer1333/amber-personal-website`
2. 上传简历：进入 `assets/resume/` 文件夹
3. 点击右上角 `Add file` -> `Upload files`
4. 把最新版简历拖进去，并改名为：

```text
resume_latest.pdf
```

5. 页面底部选择 `Commit changes`
6. 等 Streamlit Cloud 自动重新部署，通常几十秒到几分钟

项目 PDF 上传到 `assets/projects/` 文件夹，并使用下面这些文件名。文件名要完全一致，否则网页会继续显示“PDF 待补充”。

```text
audit_confirmation_summary.pdf
ipo_earnings_management.pdf
volkswagen_research.pdf
shaanxi_tourism_ipo.pdf
holiland_marketing.pdf
ai_finance_website.pdf
agi_governance_research.pdf
city_pizza_miniprogram.pdf
```

如果你是在电脑本地操作，也可以把 PDF 复制到对应文件夹后运行：

```bash
git add assets/resume/resume_latest.pdf assets/projects/
git commit -m "Add portfolio PDF assets"
git push
```

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

## How to Upload PDFs

The easiest method is to upload files directly on GitHub:

1. Open `https://github.com/starer1333/amber-personal-website`
2. For the resume, go to `assets/resume/`
3. Click `Add file` -> `Upload files`
4. Upload the latest resume and rename it to:

```text
resume_latest.pdf
```

5. Click `Commit changes`
6. Wait for Streamlit Cloud to redeploy automatically

Project PDFs should be uploaded to `assets/projects/` with these exact filenames:

```text
audit_confirmation_summary.pdf
ipo_earnings_management.pdf
volkswagen_research.pdf
shaanxi_tourism_ipo.pdf
holiland_marketing.pdf
ai_finance_website.pdf
agi_governance_research.pdf
city_pizza_miniprogram.pdf
```

If you work locally, copy the PDFs into the folders and run:

```bash
git add assets/resume/resume_latest.pdf assets/projects/
git commit -m "Add portfolio PDF assets"
git push
```
