# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 12:14:21 2025

@author: Sameer Sardar
"""

import cv2
img=cv2.imread(r"C:\Users\Sameer Sardar\Downloads\birdflock.jpg")
img1=cv2.resize(img, (600,500))

gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,thresh =cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

contours,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if (cv2.contourArea(cnt)) > 20:
        #cv2.drawContours(img1, cnt,-1, (0,255,0), 1)
        x1,y1,w,h =cv2.boundingRect(cnt)
        cv2.rectangle(img1,(x1,y1),(x1+w,y1+h),(0,255,0),2)

cv2.imshow('img',img1)
#cv2.imshow('gray',gray)

cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()