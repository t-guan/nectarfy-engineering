# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:46:16 2022

@author: Thomas
"""
#Libraries are in!
import serial;
import time;
import csv;
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue

#Initialize serial
arduino = serial.Serial(port='COM8', baudrate=9600)
arduino.flushInput()
#Initialize queues
dataQueue=Queue(maxsize=0)
ZeroData=Queue(maxsize=0)
ThreeData=Queue(maxsize=0)
TwoData=Queue(maxsize=0)
TwentyData=Queue(maxsize=0)
EightData=Queue(maxsize=0)
#Change the time value as required
t_end=time.time()+5


while time.time()<t_end:
    data=arduino.readline()
    decoded_bytes = float(data[0:len(data)-2].decode("utf-8"))
    dataQueue.put(decoded_bytes)
arduino.close()

while(dataQueue.empty()==False):
    val=dataQueue.get()
    if (val==255.0):
            with open("test_data.csv","a", newline='') as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([dataQueue.get(),dataQueue.get(),dataQueue.get(),dataQueue.get(),dataQueue.get()])
print("Done!")
        
    
            
            


    
    
        
        
    



