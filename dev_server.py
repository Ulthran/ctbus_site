#!/usr/bin/env python3
"""Development server for ctbus_site.

Serves files from the vue-frontend directory and falls back to index.html for
routes without a file extension. Useful for local SPA development.
"""

import argparse
import http.server
import os
import socketserver


class SPARequestHandler(http.server.SimpleHTTPRequestHandler):
    """Serve index.html for any path without a file extension."""

    def send_head(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) and "." not in os.path.basename(self.path):
            self.path = "/index.html"
        return super().send_head()


def run(port: int, directory: str) -> None:
    os.chdir(directory)
    handler = SPARequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving {directory} at http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run local dev server.")
    parser.add_argument("--port", "-p", type=int, default=8000)
    parser.add_argument(
        "--dir",
        "-d",
        default="vue-frontend",
        help="Directory to serve",
    )
    args = parser.parse_args()
    run(args.port, args.dir)
