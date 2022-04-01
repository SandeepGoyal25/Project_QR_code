import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("https://www.youtube.com/watch?v=TtdFq4dhGZs&t=157s")
qr.png("myfirst_QRcode.png", scale = 8)

# img = pyqrcode.make("https://www.youtube.com/watch?v=TtdFq4dhGZs&t=157s")
# img.save("QRcode.jpg")