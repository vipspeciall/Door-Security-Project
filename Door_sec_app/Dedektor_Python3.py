import cv2 as cv2
import os
import numpy as np
import threading
import RPi.GPIO as GPIO
import subprocess
from PIL import Image
import time

def pin_sinyal():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(4, GPIO.LOW)
    GPIO.cleanup()
    quit()
    

faceDetect = cv2.CascadeClassifier('/home/pi/Desktop/Door_sec_app/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0);
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("/home/pi/Desktop/Door_sec_app/recognizer/trainningData.yml")
user_id=0
kul_sayac=0
sec=0
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
num_lines = sum(1 for line in f)
f.close()
while (True):
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,3)
    cv2.imshow('Face',img)
    for(x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        user_id,conf=rec.predict(gray[y:y+h,x:x+w])
        cv2.imshow('Face',img)
        
        f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
        while(kul_sayac<num_lines):
            i = str(f.readline().split("."))
            if (user_id == str(i[0])):
                user_id= str(i[1])
            kul_sayac+=1
        f.close()
        conf = int(round(100 - conf))
        if ((conf > 40 and conf < 100) and user_id == 1):
            user_id=user_id
            #sec+=1
            #if(user_id == 'alp' and sec==5):
            print(user_id,conf)
            pin_sinyal()
                #sec=0
        elif (conf < 40):
            user_id = "unknown"
            subprocess.call(["mkdir","/home/pi/Desktop/Door_sec_app/dataSet/Unknown"])
            cv2.imwrite('/home/pi/Desktop/Door_sec_app/dataSet/Unknown/Unknown.jpg', gray[y:y+h,x:x+w])
            cevap=raw_input('Izin verilsin mi?(evet=e hayir=h): ')
            if(cevap == "e"):
                pin_sinyal()
            else:
                continue
        cv2.imshow('Face',img)
        conf=str(conf)+'%'
        kul_sayac=0    
        print(user_id,conf)
        cv2.putText(img,str(user_id),(x,y+h),font, 1,255) #Draw the text
        cv2.putText(img, str(conf), (x+5,y+h-5), font, 1, (255,255,0), 1)

    if(cv2.waitKey(1)==ord('q')):
        cam.release()
        cv2.destroyAllWindows()
        quit()
    

