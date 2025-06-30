import os
import io
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def load_env():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, val = line.split("=", 1)
                os.environ.setdefault(key.strip(), val.strip())


load_env()

PLACEHOLDERS = {
    "CDN_URL": os.environ.get("CDN_URL", ""),
    "SPOTIFY_CLIENT_ID": os.environ.get("SPOTIFY_CLIENT_ID", ""),
    "SPOTIFY_CLIENT_SECRET": os.environ.get("SPOTIFY_CLIENT_SECRET", ""),
}

ROOT = Path(__file__).resolve().parent.parent / "vue-frontend"


class ReplacingHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split("?", 1)[0].split("#", 1)[0]
        return str((ROOT / path.lstrip("/")).resolve())

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for index in ("index.html",):
                index_path = os.path.join(path, index)
                if os.path.exists(index_path):
                    path = index_path
                    break
            else:
                return super().send_head()
        ctype = self.guess_type(path)
        try:
            with open(path, "rb") as f:
                content = f.read()
        except OSError:
            return super().send_head()
        if ctype.startswith("text/") or ctype == "application/javascript":
            text = content.decode("utf-8")
            for key, value in PLACEHOLDERS.items():
                text = text.replace(key, value)
            content = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        return io.BytesIO(content)


def main():
    port = int(os.environ.get("PORT", 8000))
    server = ThreadingHTTPServer(("", port), ReplacingHandler)
    print(f"Serving on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
