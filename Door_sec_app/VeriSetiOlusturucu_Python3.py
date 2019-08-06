import cv2 
import time
import fnmatch
import os
import picamera
import subprocess
import fnmatch

detector=cv2.CascadeClassifier('/home/pi/Desktop/Door_sec_app/haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
adas_sayac=0
kul_sayac=0
yeni_kullanici=False
i='kelime'
name=input('Adinizi giriniz: ')
f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
num_lines = sum(1 for line in f)
f.close()
f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
while(kul_sayac<num_lines):
    i = str(f.readline().split(".")[1])
    
    if ((name == i[0:len(i)-1])):
        adas_sayac+=1
    kul_sayac+=1
f.close()

if(adas_sayac > 0):
    print("Ayni isimde {} adet kullanicisi var!".format(adas_sayac))
    secim=input('Yeni bir kayit mi?(evet:e hayir:h): ')
    
    if (secim == 'e'):
        subprocess.call(['mkdir', '/home/pi/Desktop/Door_sec_app/dataSet/{}.'.format(kul_sayac+1)+'{}'.format(name)])
        f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt","a+")
        f.write("{}.".format(kul_sayac+1)+"{}\n".format(name))
        f.close()
        print("Yeni kullanici fotograf klasoru olusturuldu.")
        userid=kul_sayac+1
        yeni_kullanici=True
    
    elif (secim == 'h'):
        userid=input("Id numarasini giriniz!: ")

elif (adas_sayac == 0):
    subprocess.call(['mkdir', '/home/pi/Desktop/Door_sec_app/dataSet/{}.'.format(kul_sayac+1)+'{}'.format(name)])
    print("Yeni kullanici fotograf klasoru olusturuldu.")
    f = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt","a+")
    f.write("{}.".format(kul_sayac+1)+"{}\n".format(name))
    f.close()
    yeni_kullanici=True
    userid=kul_sayac+1
    
if(yeni_kullanici==False):
    path = "/home/pi/Desktop/Door_sec_app/dataSet/{}.{}/"
    foto_sayisi = len(fnmatch.filter(os.listdir(path.format(userid,name)),'*.jpg'))
    print("Sistemde {} adet fotografiniz var!".format(foto_sayisi))

else:
    foto_sayisi = 0
    print("Sistemdeki yeni kullanici! {}".format(name))

print("Kamera Aciliyor...")    

while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,1.3,3)
    cv2.imshow('Face',img);
    for (x,y,w,h) in faces:
        cv2.imshow('Face',img);
        print("Hazir!")
        
        if(cv2.waitKey(1) & 0xFF==ord('c')):
            cv2.imwrite('/home/pi/Desktop/Door_sec_app/dataSet/{}.{}/'.format(str(userid),str(name)) + '{}.{}.{}.jpg'.format(name,str(userid),str(foto_sayisi+1)), gray[y:y+h,x:x+w])
            foto_sayisi+=1
            print("Yuz Kaydedildi!")
        
        elif(cv2.waitKey(1) & 0xFF==ord('q')):
            print("Bye Bye")
            cam.release()
            cv2.destroyAllWindows()
            quit()
    
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        print("Bye Bye")
        cam.release()
        cv2.destroyAllWindows()
        quit()
