import os
import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            df = pd.read_csv("Student_Marks.csv")

            html = """
            <html>
            <head>
                <title>Student Marks Analysis</title>
                <style>
                    body { font-family: Arial; margin: 40px; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ccc; padding: 8px; }
                    th { background: #eee; }
                </style>
            </head>
            <body>
                <h1>Cloud-Based Student Marks Analysis</h1>
                <h2>Student Marks Data</h2>
            """

            html += df.to_html(index=False)

            html += """
                <h2>Summary</h2>
                <p>Total Students: """ + str(len(df)) + """</p>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

server = HTTPServer(("0.0.0.0", PORT), Handler)
print("Server running on port", PORT)
server.serve_forever()
