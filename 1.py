# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:36:37 2021

@author: user
"""
#05/13 作業1
#110_AI班_林建名

import cv2
import numpy as np
import sys

windowsname = "Image"
cv2.namedWindow(windowsname)
shape = 100
wield = 500
background_color = (255,255,255)
color = (255, 0, 0)
speed = 3
while True:
    for motion in range(wield-shape):
        img = np.full((shape*3, wield ,3), background_color, np.uint8)
        rect = cv2.rectangle(img, (0+(motion), shape), (shape+(motion), shape*2), color, thickness=-1)
        cv2.imshow(windowsname , rect)
        if cv2.waitKey(speed) != -1:
            cv2.destroyAllWindows()
            sys.exit()
        else:
            continue
    for motion in range(wield-shape, 0, -1):
        img = np.full((shape*3, wield ,3), background_color, np.uint8)
        rect = cv2.rectangle(img, (motion, shape), (motion+shape, shape*2), color, thickness=-1)
        cv2.imshow(windowsname , rect)
        if cv2.waitKey(speed) != -1:
            cv2.destroyAllWindows()
            sys.exit()
        else:
            continue
