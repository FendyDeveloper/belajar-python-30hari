import pyqrcode
qr_code = pyqrcode.create("https://example.com")
qr_code.svg("qrcode.svg", scale=6)