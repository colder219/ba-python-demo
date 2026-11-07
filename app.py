import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/healthz", "/readyz"):
            self.send_error(404, "not found")
            return

        body = json.dumps(
            {"service": "ba-python-demo", "status": "ok", "path": self.path}
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args))


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"ba-python-demo listening on {host}:{port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
