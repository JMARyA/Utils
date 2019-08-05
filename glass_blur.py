import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])

dst = np.empty_like(img) #create empty array the size of the image
noise = cv2.randn(dst, (0,0,0), (20,20,20)) #add random img noise

# Blurring function; kernel=15, sigma=auto
pup_blur = cv2.GaussianBlur(img, (105, 105), 0)

# Pass img through noise filter to add noise
pup_noise = cv2.addWeighted(pup_blur, 0.5, noise, 0.5, 50) 

#pup_noise = cv2.GaussianBlur(pup_noise, (3, 3), 0)

cv2.imshow('Img', pup_noise)
cv2.waitKey(0)
cv2.destroyAllWindows