# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:27:45 2021

@author: babymlin
"""
#05/17作業1
#110_AI班_林建名

import numpy as np
# import cv2 as cv
import cv2

#轉HSV處理遮罩
cv2_bgr = cv2.imread("./h2.png")
# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hsv_min = np.array([0, 255, 255])
# hsv_max = np.array([0, 255, 255])
# hsv_mask = cv2.inRange(hsv_img, hsv_min, hsv_max) 
# hsvMask_output = cv2.bitwise_and(img, img, mask = hsv_mask)
  
# #轉灰階處理白底黑字
# result = cv2.subtract(hsvMask_output, (255, 255, 253, 0))
# result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# result += 255

result = cv2.absdiff(cv2_bgr, (0, 0, 255, 0))
result = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
result = cv2.multiply(result, (0, 0, 255, 0))
result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

cv2.imshow("img", result)
# cv2.imshow('hsvMask_output',hsvMask_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
cv2_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.axis("off")
plt.imshow(cv2_bgr)

background = np.full((300, 500, 3), (255, 0, 0), np.uint8)
pil_img2 = Image.fromarray(background)

plt.imshow(pil_img2)
 