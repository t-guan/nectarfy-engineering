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

#Initialize queues
dataQueue=Queue(maxsize=0)
ZeroData=Queue(maxsize=0)
ThreeData=Queue(maxsize=0)
TwoData=Queue(maxsize=0)
TwentyData=Queue(maxsize=0)
EightData=Queue(maxsize=0)

#Initialize label array
arrayLabel=[]

#Functions
def dataCollect():
    
    #Init Serial
    arduino = serial.Serial(port='COM8', baudrate=9600)
    arduino.flushInput()
    #Change the time value as required
    #Currently gives 6 full rows of data and one row of garbage values
    #Time delay after every sent packet is 500ms on Arduino End
    #May need to calc for complexity for more accurate results
    t_end=time.time()+timeCollect
    while time.time()<t_end:
        data=arduino.readline()
        decoded_bytes = float(data[0:len(data)-2].decode("utf-8"))
        dataQueue.put(decoded_bytes)
    arduino.close()
def titlePrint():
    isOverwrite=input("Do you want to overwrite existing csv?(Y/N)")
    if(isOverwrite=="Y"):
        with open("test_data.csv","w", newline='') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["TGS2600","TGS2603","TGS2602","TGS2620","TGS832A", "Label"])
    elif(isOverwrite=="N"):
        with open("test_data.csv","a", newline='') as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["TGS2600","TGS2603","TGS2602","TGS2620","TGS832A", "Label"])
    else:
        print("That is not a valid input.")
        titlePrint()                   
def dataPrint(label):
    while(dataQueue.empty()==False):
        try:
            val=dataQueue.get_nowait()
            if (val==255.0):
                try:
                    zeroval=dataQueue.get_nowait()
                except:
                    zeroval=None
                try:
                    threeval=dataQueue.get_nowait()
                except:
                    threeval=None
                try:
                    twoval=dataQueue.get_nowait()
                except:
                    twoval=None
                try:
                    twentyval=dataQueue.get_nowait()
                except:
                    twentyval=None
                try:
                    eightval=dataQueue.get_nowait()
                except:
                    eightval=None
                with open("test_data.csv","a", newline='') as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([zeroval,threeval,twoval,twentyval,eightval,label])
                ZeroData.put(zeroval)
                ThreeData.put(threeval)
                TwoData.put(twoval)
                TwentyData.put(twentyval)
                EightData.put(eightval)
        except:
            print("No more items in Queue")

#Start of Program: User Input
while True:
    try:
        timeCollect=int(input("Please enter how long to collect data per sample: "))
        break
    except:
        print("That is not an integer.")
while True:
    try:
        numSample=int(input("Please enter how many samples to collect: "))
        break
    except:
        print("That is not an integer.")
for x in range(0,numSample):
    arrayLabel.append(input("Please enter the label for sample #"+str(x+1)+": "))

titlePrint()
#Call Functions for loop
for x in range(0,numSample):
    dataCollect()
    dataPrint(arrayLabel[x])
    print("\nData for "+arrayLabel[x]+" has been collected.\n")
    if(x==numSample-1):
        print("Data collection is complete.\n")
    else:
        print("Waiting for user to collect data for "+arrayLabel[x+1]+".\n")
        input("Press Enter to proceed.")
      

print("Done!")
        
    
            
            


    
    
        
        
    



