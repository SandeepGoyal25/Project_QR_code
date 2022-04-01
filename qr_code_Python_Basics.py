import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("https://www.youtube.com/watch?v=aqvDTCpNRek&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
qr.png("Link for Pythn Basics by Harry.png", scale = 8)