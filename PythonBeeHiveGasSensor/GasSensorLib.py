# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:46:16 2022
Collects data via serialport and writes to CSV, can collect based on specific
timeframe
Collect the location and address of the Arduino board by using:
ls /dev/tty* in the terminal
@author: Thomas
"""
#Libraries are in!
import serial;
import time;
import csv;
from queue import Queue
from MLModel import gasPredictor
#Serial Port Name
     #Change the name here which will control the name in subsequent declarations
     #For Thomas' Laptop, it is COM8
     #For the RPi, it is /dev/ttyUSB0
#Initialize queues
# dataQueue=Queue(maxsize=0)
# ZeroData=Queue(maxsize=0)
# ThreeData=Queue(maxsize=0)
# TwoData=Queue(maxsize=0)
# TwentyData=Queue(maxsize=0)
# EightData=Queue(maxsize=0)
#Initialize label array
arrayLabel=[]
#Functions
def avgQueue(queue):
    size=queue.qsize()
    arraySum=0
    while True:
        try:
            arraySum=arraySum+queue.get_nowait()
        except:
            avg=float(arraySum/size)
            break
    return avg
def CreatePredArray(self, stateval,ZeroData,ThreeData,TwoData,TwentyData,EightData):
    if(stateval==1):
        #Average all the queues
        ZeroAvgVal=avgQueue(ZeroData)
        ThreeAvgVal=avgQueue(ThreeData)
        TwoAvgVal=avgQueue(TwoData)
        TwentyAvgVal=avgQueue(TwentyData)
        EightAvgVal=avgQueue(EightData)
        predArray=[ZeroAvgVal,ThreeAvgVal,TwoAvgVal,TwentyAvgVal,EightAvgVal]
    else:
        print("You will be prompted to enter five values.")
        predArray=[]
        for i in range(0, 5):
            while True:
                try:
                    val = int(input("Please input value: "))
                    break
                except:
                    print("That is not a valid integer. Try again.")
            predArray.append(val) 
    return predArray
def dataCollect(self,timeCollect,dataQ,sPort):
    #Init Serial
    #Here, the port needs to be modified.
    #/dev/ttyUSB0
    arduino = serial.Serial(port=sPort, baudrate=9600)
    arduino.flushInput()
    print("Synchronizing for sensor reading....standby")
    time.sleep(3)
    arduino.write(b'H')
    ##!! Add Safety Feedback when failrue occurs!!#
    print("Synchronization complete")
   #Change the time value as required
    #Currently gives 6 full rows of data and one row of garbage values
    #Time delay after every sent packet is 500ms on Arduino End
    #May need to calc for complexity for more accurate results
    t_end=time.time()+timeCollect
    try:
        while time.time()<t_end:
            data=arduino.readline()
            decoded_bytes = float(data[0:len(data)-2].decode("utf-8"))
            dataQ.put(decoded_bytes)
        arduino.write(b'L')
        arduino.close()
    except:
        print("\n !!!WARNING There was a data collection issue. Please reboot kernel. WARNING!!!\n")
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
def titlePrintBT():
    with open("test_data.csv","w", newline='') as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow(["TGS2600","TGS2603","TGS2602","TGS2620","TGS832A", "Label"])                 
def dataPrint(self,label,dataQueue,ZeroData,ThreeData,TwoData,TwentyData,EightData):
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
def motorRun(self,motortime,sPort):
    #Init Serial
    #The serial port in the function will have to change for the device plugged into the Arduino
    #The location of the Arduino is at /dev/ttyUSB0, and on Thomas' PC it is on "COM8"
    arduino=serial.Serial(port=sPort, baudrate=9600)
    arduino.flushInput()
    print("Synchronizing for motor control...standby")
    time.sleep(3)
    print("Sychronization complete. Motor Start...")
    arduino.write(b'M')
    time.sleep(motortime)
    arduino.write(b'O')
    print("Motor stopped.")
    arduino.close()
def ledTrigger(self,ledval,sPort):
    arduino=serial.Serial(port=sPort, baudrate=9600)
    arduino.flushInput()
    time.sleep(3)
    #Change values here
    if(ledval==0):
        arduino.write(b'A')
        print("AIR")
    if(ledval==1):
        arduino.write(b'E')
        print("ETH")
    arduino.close()
    
            
            


    
    
        
        
    



