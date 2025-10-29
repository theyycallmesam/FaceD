# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:58:54 2025

@author: Sameer Sardar
"""

#threshlding

import cv2
img=cv2.imread(r"C:\Users\Sameer Sardar\Downloads\4 ballimages.jpg")
img1=cv2.resize(img, (600,400))
img_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

adaptive_thresh=cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21, 30)
ret,simple_thresh=cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)

cv2.imshow('img',img1)
cv2.imshow('adaptivethresh',adaptive_thresh)
cv2.imshow('simplethresh',simple_thresh)
cv2.waitKey(0)