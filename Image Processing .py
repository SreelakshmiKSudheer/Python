from PIL import Image
import cv2

'''
# Flipping
#opening image
img = Image.open('Img1.png')

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a file in a human understandable format
transposed_img.save('correct.png')

print("Done")
'''

# Image Enhancing

img1 = cv2.imread('Img2.png')

# preparation for CLAHE

clahe = cv2.createCLAHE()

#convert to grey scale
gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Apply Enhancement
enh_image = clahe.apply(gray_image)

# save it to a file
cv2.imwrite('enhanced.png',enh_image)

print("Done enhancing")