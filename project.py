#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2   
import numpy as np
import time
import requests    #push
from picamera import PiCamera  #picamera
from time import sleep
camera=PiCamera()
#.xml  face and eye
face_cascade=cv2.CascadeClassifier("/home/pi/Desktop/source/masterdatahaarcascades/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("/home/pi/Desktop/source/masterdatahaarcascades/haarcascade_eye.xml")
#push server
api="https://sc.ftqq.com/SCU109071Tea37a6c411a25bb406bc05829eca44df5f325a651ad17.send"
title=u"Number_of_People(From_Camera_0)"
while(1):
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/source/imgfromcamera.jpg')
    #sleep(1)
    camera.stop_preview()
    i = cv2.imread('/home/pi/Desktop/source/imgfromcamera.jpg')
    print (i)
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    l=len(faces)
    print (l)
    nu=0
    for (x,y,w,h) in faces:
        cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
        #  cv2.putText(i,'face',(w//2+x,y-h//5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
        nu=nu+1
        cv2.putText(i,str(nu),(w//2+x,y-h//5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = i[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cv2.putText(i,"face count",(20,20),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
        cv2.putText(i,str(l),(230,20),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1) 
        
        #cv2.putText(i,"eyes count",(20,60),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
        #print (i)  #cv2.putText(i,str(r),(230,60),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
    #cv2.imshow("img",i)
    cv2.imwrite("/home/pi/Desktop/source/last_pic.jpg",i)#save img 
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    count= int(nu)
    content="Time:"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n\nID:Camera Pi0" +"\n\nNumber:" +str(count)
    data={
        "text":title,
        "desp":content
        }
    req=requests.post(api,data=data)
    sleep(1) #RUN Cycle 20s
#cv2.waitKey(0) 


