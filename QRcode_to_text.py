# import cv2
# d = cv2.QRCodeDetector()
# val, _, _ = d.detectAndDecode(cv2.imread("MyQRcode.jpg"))
# print("Decoded Text is : ", val)
import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("Telecoma_playlist_QRcode.jpg"))
print("Decoded Text is : ", val)
