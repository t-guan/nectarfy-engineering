# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:46:16 2022
Collects data via serialport and writes to CSV, can collect based on specific
timeframe

@author: Thomas
"""
#Libraries are in!
import serial;
import time;
import csv;
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
#Currently gives 6 full rows of data and one row of garbage values
#Time delay after every sent packet is 500ms on Arduino End
#May need to calc for complexity for more accurate results
t_end=time.time()+5
while time.time()<t_end:
    data=arduino.readline()
    decoded_bytes = float(data[0:len(data)-2].decode("utf-8"))
    dataQueue.put(decoded_bytes)
arduino.close()
with open("test_data.csv","a", newline='') as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow(["TGS2600","TGS2603","TGS2602","TGS2620","TGS832A"])
while(dataQueue.empty()==False):
    try:
        val=dataQueue.get_nowait()
        if (val==255.0):
            try:
                zeroval=dataQueue.get_nowait()
            except:
                zeroval=0
            try:
                threeval=dataQueue.get_nowait()
            except:
                threeval=0
            try:
                twoval=dataQueue.get_nowait()
            except:
                twoval=0
            try:
                twentyval=dataQueue.get_nowait()
            except:
                twentyval=0
            try:
                eightval=dataQueue.get_nowait()
            except:
                eightval=0
            with open("test_data.csv","a", newline='') as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([zeroval,threeval,twoval,twentyval,eightval])
            ZeroData.put(zeroval)
            ThreeData.put(threeval)
            TwoData.put(twoval)
            TwentyData.put(twentyval)
            EightData.put(eightval)
    except:
        print("No more items in Queue")

print("Done!")
        
    
            
            


    
    
        
        
    



