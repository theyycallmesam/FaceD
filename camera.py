# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 13:17:27 2025

@author: Sameer Sardar
"""

import cv2

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 
cap.release()

cv2.destroyAllWindows()
    