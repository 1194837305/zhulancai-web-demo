# 本地运行与宝塔部署

## 本地运行

下载 Release 完整包并解压，在根目录运行：

```bash
python tools/verify_demo.py
python tools/serve_demo.py
```

Linux / macOS 使用 `python3`。本地服务绑定 `127.0.0.1`，控制台会显示可访问的地址。关闭服务按 Ctrl+C。无需安装 Godot。

## 宝塔 Nginx

1. 在完整包根目录运行 `python tools/prepare_gzip.py`，生成对应的预压缩文件。
2. 备份原网站运行文件，将 `web/` 内的文件上传到游戏站点根目录。仅上传 `web/` 的内容。
3. 替换新版时，`.pck` 与 `.pck.gz` 必须成对更新，HTML 中的大小配置也要匹配。
4. 保留已有证书设置和 HTTPS。

Nginx 游戏站点的 `server` 层需要：

```nginx
add_header Cross-Origin-Opener-Policy "same-origin" always;
add_header Cross-Origin-Embedder-Policy "require-corp" always;
add_header Cache-Control "no-cache" always;
```

游戏文件所在的静态 `location` 中启用 `gzip_static on;`、`gzip_vary on;`。确保 `.wasm` 使用 `application/wasm`，`.js` 使用 JavaScript MIME 类型。请与现有宝塔配置合并，保留证书验证路径，避免重复 location 块或其他静态规则覆盖响应头。

上线后在页面控制台检查 `window.crossOriginIsolated` 是否为 `true`。GitHub 展示仓库不会自动部署到宝塔。

## 包体说明

Release ZIP 仅包含原始游戏文件，不重复放入 `.gz`，减少下载及上传包体。ZIP 解压后会恢复完整文件；Nginx 使用的 `.gz` 可通过工具在部署前重新生成。
