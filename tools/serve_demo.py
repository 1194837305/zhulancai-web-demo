"""Serve the frozen Web Demo locally with cross-origin isolation headers."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, '.wasm': 'application/wasm'}

    def accepts_gzip(self):
        encodings = {}
        for item in self.headers.get('Accept-Encoding', '').split(','):
            token, *parameters = item.strip().lower().split(';')
            quality = 1.0
            try:
                for parameter in parameters:
                    if parameter.strip().startswith('q='): quality = float(parameter.strip()[2:])
            except ValueError:
                quality = 0.0
            encodings[token] = quality
        return 0 < encodings.get('gzip', encodings.get('*', 0)) <= 1

    def send_head(self):
        original = self.path
        parts = urlsplit(original)
        self._gzip = False
        self._etag = None
        path = Path(self.translate_path(original))
        if self.accepts_gzip() and path.is_file() and Path(str(path)+'.gz').is_file():
            self.path = urlunsplit(parts._replace(path=parts.path+'.gz'))
            path = Path(str(path)+'.gz'); self._gzip = True
        if path.is_file():
            stat = path.stat()
            self._etag = f'"{stat.st_mtime_ns:x}-{stat.st_size:x}"'
            if self.headers.get('If-None-Match') == self._etag:
                self.send_response(304); self.end_headers(); self.path = original
                return None
        try:
            return super().send_head()
        finally:
            self.path = original

    def guess_type(self, path):
        return super().guess_type(path[:-3] if getattr(self, '_gzip', False) and path.endswith('.gz') else path)

    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Vary', 'Accept-Encoding')
        if getattr(self, '_gzip', False): self.send_header('Content-Encoding', 'gzip')
        if getattr(self, '_etag', None): self.send_header('ETag', self._etag)
        super().end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8768)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parents[1] / 'web')
    args = parser.parse_args()
    directory = args.directory.resolve()
    if not (directory / 'index.html').is_file():
        parser.error('Game files missing. Download Zhulancai-Web-Demo-20261103.zip from GitHub Releases.')
    from verify_demo import verify
    try:
        verify(directory)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(directory)))
    except OSError as error:
        if getattr(error, 'winerror', None) != 10048 and error.errno != 98:
            raise
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(directory)))
    print(f'Web test: http://127.0.0.1:{server.server_port}/', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
