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
from MLModel import gasPredictor

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
motortimeCollect=5
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
def CreatePredArray(stateval):
    if(stateVal==1):
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
def dataCollect():
    #Init Serial
    arduino = serial.Serial(port='COM8', baudrate=9600)
    arduino.flushInput()
    print("Synchronizing for sensor reading....standby")
    time.sleep(3)
    arduino.write(b'H')
    print("Synchornization complete")
    #Change the time value as required
    #Currently gives 6 full rows of data and one row of garbage values
    #Time delay after every sent packet is 500ms on Arduino End
    #May need to calc for complexity for more accurate results
    t_end=time.time()+timeCollect
    try:
        while time.time()<t_end:
            data=arduino.readline()
            decoded_bytes = float(data[0:len(data)-2].decode("utf-8"))
            dataQueue.put(decoded_bytes)
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
def motorRun():
    #Init Serial
    arduino=serial.Serial(port='COM8', baudrate=9600)
    arduino.flushInput()
    print("Synchronizing for motor control...standby")
    time.sleep(3)
    print("Sychronization complete. Motor Start...")
    arduino.write(b'M')
    time.sleep(motortimeCollect)
    arduino.write(b'O')
    print("Motor stopped.")
    arduino.close()
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
            motorRun()
            dataCollect()
            dataPrint(arrayLabel[x])
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
            print("There was more than one sample collected. Defaulting to manual entry.")
            stateVal=0
        predArray=CreatePredArray(stateVal)
        Pred=gasPredictor(predArray)
        print("The prediction is "+Pred)
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
        
    
            
            


    
    
        
        
    



