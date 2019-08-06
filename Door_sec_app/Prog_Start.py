import tkinter as tk
import subprocess 

import time
import cv2

import time

def recording():
    print("Prepare for picture")
    /#subprocess.call(["sudo","modprobe","bcm2835-v4l2"])
    subprocess.call(["python3","VeriSetiOlusturucu_Python3.py","-j4"])

def trainning():
    print("Veriler egitiliyor...")
    subprocess.call(["python","Egitici_Python3.py"])
    
def main_program():
    print("Guvenlik sistemi aciliyor...")
   /#subprocess.call(["sudo","modprobe","bcm2835-v4l2"])
    subprocess.call(["python","Dedektor_Python3.py","-j4"])
    

def quitting():
    print("Bye Bye!")
    quit()
    
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300) 
canvas1.pack()

print("Hos Geldiniz!")

kayit = tk.Button(root, text="Yuz Kaydet!", command=recording)

egitim = tk.Button(root, text="Yuzleri Egit!", command=trainning)

main_program = tk.Button(root, text="Sistemi Baslat!", command=main_program)

cikis = tk.Button(root, text="Cikis", fg="red", command=quitting)

canvas1.create_window(150,50, window=kayit)
canvas1.create_window(150,100, window=egitim)
canvas1.create_window(150,150, window=main_program)
canvas1.create_window(150, 200, window=cikis)

root.mainloop()
