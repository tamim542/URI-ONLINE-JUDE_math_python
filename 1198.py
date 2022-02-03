import signal
import sys
import time

run = True

def signal_handler(signal, frame):
    global run
    print ("exiting")
    run = False

signal.signal(signal.SIGINT, signal_handler)
while run:

    time.sleep(1)
    while True:
        x = int(input())
        y = int(input())
        if x < y:
            print(y - x)
        else:
            print(x - y)




'''while True:
    try:
        while True:
            x=int(input())
            y = int(input())
            if x < y:
                print( y - x)
            else :
                print( x - y )
    except EOFERROR:
        break
'''