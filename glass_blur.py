import cv2
import numpy as np
import sys
import os

def blurImage(path):
    img = cv2.imread(path)

    dst = np.empty_like(img) #create empty array the size of the image
    noise = cv2.randn(dst, (0,0,0), (20,20,20)) #add random img noise

    # Blurring function; kernel=15, sigma=auto
    pup_blur = cv2.GaussianBlur(img, (105, 105), 0)

    # Pass img through noise filter to add noise
    pup_noise = cv2.addWeighted(pup_blur, 0.5, noise, 0.5, 50) 

    cv2.imwrite(os.path.splitext(path)[0]+".blur.jpg", pup_noise)

def blurImageRet(path):
    img = cv2.imread(path)

    dst = np.empty_like(img) #create empty array the size of the image
    noise = cv2.randn(dst, (0,0,0), (20,20,20)) #add random img noise

    # Blurring function; kernel=15, sigma=auto
    pup_blur = cv2.GaussianBlur(img, (105, 105), 0)

    # Pass img through noise filter to add noise
    pup_noise = cv2.addWeighted(pup_blur, 0.5, noise, 0.5, 50) 

    return pup_noise

if __name__ == "__main__":
    blurImage(sys.argv[1])