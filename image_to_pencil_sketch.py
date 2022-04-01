import cv2
from cv2 import pencilSketch
# from numpy import imag
#reading image
image = cv2.imread("Shrey.jpg")

#converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencilSketch = cv2.divide(gray_image, inverted_image, scale=256.0)
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Shrey", pencilSketch)
cv2.waitKey(0)