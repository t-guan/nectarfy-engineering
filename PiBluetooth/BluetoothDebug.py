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
def press_1(pos):
    print("BLOOOOOO")
def press_2(pos):
    print("GREEEEEEEEEEE")
def press_3(pos):
    print("REEEEEEEEEEEEED")
while True:
    bd[0,0].when_pressed=press_1
    bd[2,0].when_pressed=press_2
    bd[4,0].when_pressed=press_3
