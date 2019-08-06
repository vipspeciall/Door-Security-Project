import cv2,os
import os
import numpy as np
from PIL import Image 

recognizer = cv2.face.LBPHFaceRecognizer_create()
dosya=0
top_faces=[]
top_IDs=[]
def getImagesWithID(path):
     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
     faces=[]     
     IDs=[]    
     for imagePath in imagePaths:
          faceImg=Image.open(imagePath).convert('L');
          faceNp=np.array(faceImg,'uint8')
          ID=int(os.path.split(imagePath)[-1].split('.')[1])
          faces.append(faceNp)
          print (ID)
          IDs.append(ID)
          cv2.imshow("traning",faceNp)
          cv2.waitKey(10)
     return IDs, faces
file = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
kullanici = sum(1 for line in file)
file.close()
file = open("/home/pi/Desktop/Door_sec_app/dataSet/users.txt")
while(dosya<kullanici):
    folders=file.readline()
    folders=folders[0:len(folders)-1]
    path = '/home/pi/Desktop/Door_sec_app/dataSet/{}'.format(folders)
    IDs,faces=getImagesWithID(path)
    top_IDs+=IDs
    top_faces+=faces
    dosya+=1

recognizer.train(top_faces,np.array(top_IDs))
recognizer.write('/home/pi/Desktop/Door_sec_app/recognizer/trainningData.yml')    
print("Islem tamam!")
cv2.destroyAllWindows()
