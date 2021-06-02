# -*- coding: utf-8 -*-
"""
Created on Mon May 17 08:36:46 2021

@author: babymlin
"""

#05/27作業1
#110_AI班_林建名

# import numpy as np
import cv2

video = cv2.VideoCapture("./h3.mp4")
#_, first_frame = video.read()
markColor=(0, 0, 255)

while video.isOpened():
    ret, frame = video.read()
    if ret == False:
        break
    #diff = cv2.absdiff(first_frame, frame)
    #gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #binary = cv2.inRange(gray, 80, 255,)
    binary = cv2.inRange(frame, (0,75,75), (255,255,255))
    binary = cv2.bitwise_not(binary)
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #抓輪廓
    # print(f"{contours}\n{hierarchy}")
    for c in contours:
        #print(len(c))
        (x, y, w, h) = cv2.boundingRect(c)
        if w > h*1.5 and len(c) >= 400:
            cv2.rectangle(frame, (x,y), (x+w,y+h), markColor, 2)
    cv2.imshow("Video", frame)
    if cv2.waitKey(33) != -1:
        break
cv2.destroyAllWindows()