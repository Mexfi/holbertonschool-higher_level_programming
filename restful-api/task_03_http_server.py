import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Sadece GET isteğini işlemek için BaseHTTPRequestHandler'dan türetilmiş sınıf
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # İstek yoluna göre işlem yapıyoruz
        if self.path == "/":
            # Ana sayfaya gelen isteğe yanıt
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!"

        elif self.path == "/data":
            # /data yoluna gelen isteğe JSON yanıtı gönderiyoruz
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # JSON formatında veri
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # JSON verisini yanıt olarak gönderiyoruz
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            # /status yoluna gelen isteğe durum yanıtı gönderiyoruz
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Durum JSON verisi
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))

        else:
            # Tanımlanmamış yollar için 404 yanıtı
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Sunucu çalıştırma fonksiyonu
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

# Sunucuyu başlatmak için ana işlev
if __name__ == "__main__":
    run()
