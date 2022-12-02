from tkinter import *
import serial
import time
import threading


global Cara1
global Cara2

arduino= serial.Serial('COM3', 9600)
time.sleep(2)
        
#Función para lectura de sensores
def Lectura():
    global Cara1
    global Cara2
while True:
    cad =arduino.readline().decode('ascii').strip()
    pos=cad.index(":")
    Button=cad[:pos] #Desde inicio hasta POS
    #print (label)
                    
    if Button == "Cara1":
        print("Error")
    elif Button == "Cara2":
        print("Correcto")
    elif Button == "Cara3":
        print("Error")
    elif Button == "Cara4":
        