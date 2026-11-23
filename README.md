# 超时空校长、于猪栏菜中重生 · Web Demo

校园日程、人物相遇与答辩比赛交织的大学生活试玩。

[**在线试玩**](https://game.zuelgal.club/) · [**下载完整 Demo**](https://github.com/1194837305/zhulancai-web-demo/releases/download/web-demo-20261103/Zhulancai-Web-Demo-20261103.zip) · [社团门户](https://zuelgal.club/) · [发布与运行说明](docs/PUBLISH.md)

![标题宣传图](docs/images/promo.png)

## 试玩内容

- 前两个学年的校园日程、角色剧情与比赛玩法。
- 包含此 Demo 版本的 614 条配音资源。
- 剧情支持历史记录、自动播放、快进及存档。
- 第二年正常结算后进入 Demo 结束页，试玩范围内的失败结局保留。

内容快照：**2026-11-03**；仓库整理日期：**2026-11-23**。本仓库只分发这份已导出的 Web Demo，不跟随后续本地开发版本更新，不包含完整 Godot 编辑工程。

## 直接游玩

打开 **https://game.zuelgal.club/**。推荐电脑端新版 Chrome / Edge，首次下载主要资源约 374 MB，下载后仍需准备首次画面。多线程版需要浏览器支持安全上下文、跨源隔离和 SharedArrayBuffer；部分手机或应用内浏览器可能无法启动。

存档保存在当前浏览器的网站本地数据中，不会自动跨设备同步。清除网站数据可能导致存档丢失。

## 下载后本地运行

1. 在本仓库的 **Releases** 中下载 `Zhulancai-Web-Demo-20261103.zip`，完整解压。
2. 安装 Python 3.10 或更新版本。
3. Windows 双击 `start-demo.cmd`；其他系统在解压目录运行：

   ```bash
   python3 tools/serve_demo.py
   ```

4. 打开终端输出的本地地址。默认端口为 8768，已占用时会自动选用空闲端口。

请通过本地 HTTP 服务运行，不要直接双击 `web/index.html`。本地服务自带多线程所需响应头。

> GitHub 自动生成的 **Source code ZIP** 和普通仓库克隆，只含作品展示、运行工具和文件清单。完整游戏资源放在 Release 附件中；请下载上面指定的完整试玩 ZIP。

## 项目画面

![Demo 标题画面](docs/images/title.png)

上图为同版本原生运行时的标题页截图，网页版使用相同标题素材。

## 发布结构

```text
README.md                    作品介绍与在线试玩入口
release-manifest.json        已冻结 Web 文件的大小与 SHA-256
start-demo.cmd               Windows 本地启动
web/                         完整游戏文件，仅随 Release 分发
licenses/                    从本 Demo 资源包提取的原始授权记录
tools/                       本地服务、完整性检查和 gzip 生成工具
docs/                        GitHub 发布、宝塔部署及版本说明
```

技术栈：Godot 4.7.2 / WebAssembly / WebGL 2 / 多线程 Web 导出。这里展示的是试玩发布工程，不是可编辑的游戏源码仓库。

## 部署

现有试玩站点使用宝塔 Nginx。部署前可运行 `python tools/prepare_gzip.py`，然后将 `web/` 的内容上传到站点根目录。HTTPS、WASM 类型和隔离响应头的具体配置见 [部署说明](docs/DEPLOY.md)。

本项目没有提供可直接一键启用的 GitHub Pages 游戏部署：现有多线程导出依赖 COOP / COEP 响应头。GitHub 负责作品展示与下载分发，在线试玩入口仍使用现有站点。

## 授权与署名

游戏剧情、美术、配音等内容的权利归原作者或相应权利人所有。本仓库不额外授予修改游戏内容、提取素材或商业再分发的许可。第三方组件和素材按各自许可使用，原始授权记录见 [licenses/](licenses/) 与 [授权说明](LICENSE.md)。
