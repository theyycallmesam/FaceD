# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 13:30:46 2025

@author: Sameer Sardar
"""

import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Sameer Sardar\Pictures\Saved Pictures\e7b5a370-db98-4531-a592-66f5a08efff0.jpg")

img_edge=cv2.Canny(img,100,200)

img_edge_d=cv2.dilate(img_edge,np.ones((3,3),dtype=np.int8))

img_edge_e=cv2.erode(img_edge_d,np.ones((3,3),dtype=np.int8))
                      
cv2.imshow('img',img)
cv2.imshow('img_edge',img_edge)
cv2.imshow('img_edge_d',img_edge_d)
cv2.imshow('im_edge_e',img_edge_e)

cv2.waitKey(0)