"""Local preview that mimics Vercel cleanUrls (extensionless routes).

    python preview.py     ->  http://localhost:8080
"""
import http.server
import os
import socketserver

PORT = 8082
REDIRECTS = {
    "/blog": "/slot-malaysia",
    "/promotion": "/711cuci-malaysia-guide",
    "/promo": "/711cuci-malaysia-guide",
    "/login": "/slot-malaysia-mega888-login-problem-fix-guide",
    "/register": "/how-to-register",
    "/t&c": "/terms-and-conditions",
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        if path in REDIRECTS:
            self.send_response(301)
            self.send_header("Location", REDIRECTS[path])
            self.end_headers()
            return
        if path not in ("/", "") and not os.path.splitext(path)[1]:
            candidate = path.lstrip("/") + ".html"
            if os.path.exists(candidate):
                self.path = "/" + candidate
        return super().do_GET()

    def log_message(self, fmt, *args):
        pass


os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("preview running: http://localhost:%d" % PORT)
    httpd.serve_forever()