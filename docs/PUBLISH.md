# 发布到 GitHub

## 1. 创建作品展示仓库

在 GitHub 创建空仓库，例如 `zhulancai-web-demo`。把“GitHub 项目包 ZIP”解压，打开里面的项目文件夹。

可以通过 GitHub 网页的 **Add file → Upload files** 上传解压后的文件和文件夹；不要把项目 ZIP 本身当成源码上传。

也可以在项目目录使用 Git：

```bash
git init -b main
git add .
git commit -m "Publish two-year Web Demo portfolio"
git remote add origin https://github.com/你的用户名/zhulancai-web-demo.git
git push -u origin main
```

`.gitignore` 会排除 `web/` 的完整运行文件，仅保留 `web/README.md`。无需配置 Git LFS。

## 2. 上传完整游戏包

进入仓库 **Releases → Create a new release**：

- Tag：`web-demo-20261103`
- Title：`前两年 Web Demo · 2026-11-03`
- 正文可使用本目录的 `RELEASE_NOTES.md`。
- 附件上传本次提供的 **`Zhulancai-Web-Demo-20261103.zip`**。

用户从 Releases 下载这个完整试玩包，而不是 GitHub 自动生成的 Source code ZIP。仓库 README 已按这个文件名说明下载方式，不需要预填仓库名。

## 3. 完成展示

仓库 About 可填写：

> 校园题材大学生活游戏：前两年 Web Demo，包含剧情、日程、答辩比赛与配音。

Website 填：`https://game.zuelgal.club/`。

仓库描述与截图不会自动更改宝塔网站，也不会发布后续本地开发版。

## 验证范围

整理前已校验冻结 Web 包与原构建清单的 SHA-256 一致。本次仅整理发布方式，没有重导出或修改玩法。完整游戏文件的清单见根目录 `release-manifest.json`。

GitHub 的大文件政策：https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
