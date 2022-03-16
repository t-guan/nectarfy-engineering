from bluedot import BlueDot
bd=BlueDot(cols=3,rows=3)
while True:
    bd[0,0].wait_for_press()
    print("PRESS")
    bd[1,1].wait_for_press()
    print("PRESSTWO")
