# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:25:43 2022
Just tryin something sneaky out heh
@author: Thomas Guan
"""
#Libraries are in!
import serial;
import time;
import csv;
from queue import Queue
from MLModel import gasPredictor
from GasSensorLib import titlePrint,motorRun,dataCollect,dataPrint,CreatePredArray,ledTrigger
#Serial Port Name
     #Change the name here which will control the name in subsequent declarations
     #For Thomas' Laptop, it is COM8
     #For the RPi, it is /dev/ttyUSB0
sPort='COM3'
#Initialize queues
dataQueue=Queue(maxsize=0)
ZeroData=Queue(maxsize=0)
ThreeData=Queue(maxsize=0)
TwoData=Queue(maxsize=0)
TwentyData=Queue(maxsize=0)
EightData=Queue(maxsize=0)
#Initialize label array
arrayLabel=[]
#State Value Variables
stateVal=0
numSample=0
motortimeCollect=10
timeCollect=0

#Start of Program: Ask for state of program:
while True:
    state=input("Please select: Collection mode(C) or Prediction Mode(P) or Quit(Q)\n")
    #Collection Mode
    if(state=="C"):
        input("Entering collection mode. Press enter to continue.")
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
            motorRun(motorRun,motortimeCollect,sPort)
            dataCollect(dataCollect,timeCollect,dataQueue,sPort)
            dataPrint(dataPrint,arrayLabel[x],dataQueue,ZeroData,ThreeData,TwoData,TwentyData,EightData)
            print("\nData for "+arrayLabel[x]+" has been collected.\n")
            if(x==numSample-1):
                print("Data collection is complete.\n")
                arrayLabel.clear()
            else:
                print("Waiting for user to collect data for "+arrayLabel[x+1]+".\n")
                input("Press Enter to proceed.")
    elif(state=="P"):
        #Prediction Mode
        input("Entering prediction mode. Press enter to continue.")
        if(numSample==1):
            print("Singular collection entry detected. Defaulting to collected data.")
            stateVal=1
        else:
            print("Defaulting to manual entry.")
            stateVal=0
        predArray=CreatePredArray(CreatePredArray,stateVal,ZeroData,ThreeData,TwoData,TwentyData,EightData)
        Pred=gasPredictor(predArray)
        print("The prediction is "+Pred[0])
        ledTrigger(ledTrigger, Pred[1],sPort)
        stateVal=0
    elif(state=="O"):
        print("Change the motor runtime\n")
        print("The default runtime is currently 10 seconds")
        motortimeCollect=int(input("Please enter new value"))
        input("The current motor runtime has been changed. Press Enter to continue")
    elif(state=="Q"):
        print("Quitting...")
        break
    else:
        print("That is not a valid entry. Please try again: ")

print("GoodBye!")