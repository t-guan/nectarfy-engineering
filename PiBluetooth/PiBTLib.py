# -*- coding: utf-8 -*-
"""
Created on Wed Mar  16 2022
HoldsBluedot Libraries
@author: Thomas
"""
#Import Bluedot Libraries
from bluedot import BlueDot
#Setup Bluedot
bd=BlueDot(cols=5)
#Hide the two buttons for separation
bd[1,0].visible=False
bd[3,0].visible=False
#Change colors
bd[2,0].color="green"
bd[4,0].color="red"
#Define Presssed Function to catch any button press
def pressed(pos):
    print("Button {}.{} pressed".format(pos.col,pos.row))

    
