#!/usr/bin/python3
"""
simple API using Python's http.server
"""

import json
import http.server
import socketserver

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    """
    custom request
    """
    def do_GET(self):
        """
        handles GET request
        """
        path = self.path
        if '/data' in path:
            dic = {"name": "John", "age": 30, "city": "New York"}
            new_dic = json.dumps(dic)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(new_dic.encode('utf-8'))
        elif '/info' in path:
            dic = {"version": "1.0", "description": "A simple API\
                   built with http.server"}
            new_dic = json.dumps(dic)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(new_dic.encode('utf-8'))
        elif '/' == path:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif '/status' == path:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
