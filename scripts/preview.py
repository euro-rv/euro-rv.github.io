#!/usr/bin/env python3
"""Lightweight local preview for the Euro-RV Jekyll site (no Ruby required)."""

from __future__ import annotations

import argparse
import http.server
import re
import socketserver
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PORT = 4000


def ensure_markdown():
    try:
        import markdown  # noqa: F401
    except ImportError:
        import subprocess

        print("Installing preview dependency: markdown", file=sys.stderr)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "markdown"],
        )
        import markdown  # noqa: F401


def load_title() -> str:
    config = ROOT / "_config.yaml"
    if not config.exists():
        return "Euro-RV Workshop"

    for line in config.read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip()
    return "Euro-RV Workshop"


def preprocess_jekyll(content: str) -> str:
    content = re.sub(
        r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}",
        r"\1",
        content,
    )
    content = re.sub(r"\{:\s*[^}]+\}", "", content)
    content = re.sub(r"<!--\s*index\.md\s*-->\s*", "", content, count=1)
    return content


def render_page() -> bytes:
    ensure_markdown()
    import markdown

    index = ROOT / "index.md"
    if not index.exists():
        raise FileNotFoundError(f"Missing {index}")

    body = markdown.markdown(
        preprocess_jekyll(index.read_text(encoding="utf-8")),
        extensions=["extra", "sane_lists", "tables"],
        output_format="html5",
    )

    title = load_title()
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-light.min.css">
  <style>
    body {{
      box-sizing: border-box;
      min-width: 200px;
      max-width: 980px;
      margin: 0 auto;
      padding: 45px;
    }}
    @media (max-width: 767px) {{
      body {{ padding: 15px; }}
    }}
    .markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; }}
    .preview-banner {{
      background: #fff8e1;
      border: 1px solid #ffe082;
      border-radius: 6px;
      color: #6d4c00;
      font-size: 0.85rem;
      margin-bottom: 1.5rem;
      padding: 0.5rem 0.75rem;
    }}
  </style>
</head>
<body>
  <div class="markdown-body">
    <div class="preview-banner">Local preview (Python). For exact GitHub Pages output, run <code>bundle exec jekyll serve</code>.</div>
    {body}
  </div>
</body>
</html>
"""
    return html.encode("utf-8")


class PreviewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]

        if path in ("", "/"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(render_page())
            return

        file_path = (ROOT / path.lstrip("/")).resolve()
        if not str(file_path).startswith(str(ROOT.resolve())):
            self.send_error(403)
            return

        if file_path.is_file():
            content_type = "application/octet-stream"
            if file_path.suffix == ".svg":
                content_type = "image/svg+xml"
            elif file_path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
                content_type = f"image/{file_path.suffix.lstrip('.')}"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(file_path.read_bytes())
            return

        self.send_error(404)

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), fmt % args))


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview the Euro-RV site locally.")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--no-open", action="store_true", help="Do not open a browser tab.")
    args = parser.parse_args()

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    with ReusableTCPServer(("", args.port), PreviewHandler) as httpd:
        url = f"http://127.0.0.1:{args.port}/"
        print(f"Preview server running at {url}")
        print("Press Ctrl+C to stop.")
        if not args.no_open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
