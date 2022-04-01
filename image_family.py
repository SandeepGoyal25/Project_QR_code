# import cv2
# from cv2 import pencilSketchx
# def img2sketch(photo, k_size):
#     #Read Image
#     img=cv2.imread(photo)
    
#     # Convert to Grey Image
#     grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Invert Image
#     invert_img=cv2.bitwise_not(grey_img)
#     #invert_img=255-grey_img

#     # Blur image
#     blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

#     # Invert Blurred Image
#     invblur_img=cv2.bitwise_not(blur_img)
#     #invblur_img=255-blur_img

#     # Sketch Image
#     sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

#     # Save Sketch 
#     cv2.imwrite('sketch.png', sketch_img)

#     # Display sketch
#     cv2.imshow('sketch image',sketch_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    
# #Function call
# img2sketch(photo='image.png', k_size=7)

# import cv2
# image = cv2.imread("Shrey.jpeg")
# grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# invert = cv2.bitwise_not(grey_img)
# blur = cv2.GaussianBlur(invert, (21, 21), 0)
# invertedblur = cv2.bitwise_not(blur)
# sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
# cv2.imwrite("Shrey_sketch.png", sketch)

import cv2
image = cv2.imread("Family_pic.jpeg")
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("Family_pic_sketch.jpeg", sketch)

