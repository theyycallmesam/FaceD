# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:27:26 2025

@author: Sameer Sardar
"""

import cv2
import os

video_path=os.path.join('.','data',r"C:\Minal wedding\01\IMG_0133.MP4")
video=cv2.VideoCapture(video_path)                       
ret = True

while ret:
    ret,frame= video.read()
    if ret:
        cv2.imshow('frame',frame) 
        cv2.waitKey(40)
    
video.release()
cv2.destryAllWindows()    
                       