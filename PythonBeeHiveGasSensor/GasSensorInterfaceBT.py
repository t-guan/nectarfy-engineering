# -*- coding: utf-8 -*-
"""
Created on Wed Mar  16 2022
Does the same stuff as GasSensorInterface, but boiled down to be controlled via bluedot
@author: Thomas
"""
#Libraries are in!
import serial;
import time;
import csv;
from queue import Queue
from MLModel import gasPredictor
from GasSensorLib import titlePrintBT,motorRun,dataCollect,dataPrint,CreatePredArray
#BlueDot Setup
from bluedot import BlueDot
#Setup Bluedot
bd=BlueDot(cols=5)
#Hide the two buttons for separation
bd[1,0].visible=False
bd[3,0].visible=False
#Change colors
bd[2,0].color="green"
bd[4,0].color="red"

#Serial Port Name
     #Change the name here which will control the name in subsequent declarations
     #For Thomas' Laptop, it is COM8
     #For the RPi, it is /dev/ttyUSB0
sPort='/dev/ttyUSB0'
#Initialize queues
dataQueue=Queue(maxsize=0)
ZeroData=Queue(maxsize=0)
ThreeData=Queue(maxsize=0)
TwoData=Queue(maxsize=0)
TwentyData=Queue(maxsize=0)
EightData=Queue(maxsize=0)
#Initialize label array
arrayLabel=[]
#State Value Variable
stateVal=0
numSample=0
killvar=0
#Modify these variables if needed
motortimeCollect=60
timeCollect=30
#Create exception
class Exit(Exception): pass
#Program comprised of functions based on BlueDot functionality
def Collect(pos):
    timeCollect=30
    arrayLabel.append("CollectedData")
    titlePrintBT()
    #Just run once
    motorRun(motorRun,motortimeCollect,sPort)
    dataCollect(dataCollect,timeCollect,dataQueue,sPort)
    dataPrint(dataPrint,arrayLabel[0],dataQueue,ZeroData,ThreeData,TwoData,TwentyData,EightData)
    print("\nData for "+arrayLabel[0]+" has been collected.\n")
    print("Back at main")
def Predict(pos):
    stateVal=1
    predArray=CreatePredArray(CreatePredArray,stateVal,ZeroData,ThreeData,TwoData,TwentyData,EightData)
    Pred=gasPredictor(predArray)
    print("The prediction is "+Pred)
    stateVal=0
    print("Back at Main")
def Kill(pos):
    raise Exit
#Start of Program: Ask for state of program:
try:
    while True:
        bd[0,0].when_pressed=Collect  
        bd[2,0].when_pressed=Predict
        bd[4,0].when_pressed=Kill
except Exit:
    print("GoodBye!")
        
    
            
            


    
    
        
        
    



