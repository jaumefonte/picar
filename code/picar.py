


import RPi.GPIO as GPIO
import time

left_R = 22
left_G = 23
left_B = 24

right_R = 10
right_G = 9
right_B = 25

on  = GPIO.LOW
off = GPIO.HIGH

def both_on():
    GPIO.output(left_R, on)
    GPIO.output(left_G, on)
    GPIO.output(left_B, on)

    GPIO.output(right_R, on)
    GPIO.output(right_G, on)
    GPIO.output(right_B, on)

def setup():#initialization
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_R, GPIO.OUT)
    GPIO.setup(left_G, GPIO.OUT)
    GPIO.setup(left_B, GPIO.OUT)
    GPIO.setup(right_R, GPIO.OUT)
    GPIO.setup(right_G, GPIO.OUT)
    GPIO.setup(right_B, GPIO.OUT)
    both_off()

def both_off():
    GPIO.output(left_R, off)
    GPIO.output(left_G, off)
    GPIO.output(left_B, off)

    GPIO.output(right_R, off)
    GPIO.output(right_G, off)
    GPIO.output(right_B, off)


def PrintVersion():
    print("Version 0.0.1")
    
def PrintHelp():
    print("exit\t\tCloses program. \nversion\t\tPrints version number.")

def FrontLightsOn():
    print("Front lights ON")
    both_on()

def FrontLightsOff():
    print("Front lights OFF")
    both_off()

running = True
setup()
FrontLightsOn()
try:    
    while(running):
        command = input('PICAR >')
        if(command == 'exit'):
            running = False
        elif(command == 'help'):
            PrintHelp()
        elif(command == 'version'):
            PrintVersion()
        else:
            print("'"+command +"' is not a valid command. Type 'help' for available commands.")
except KeyboardInterrupt:
    print("bye")
    
FrontLightsOff()
print("PICAR cerrado. Pulsa 'Enter' para salir")
input()

    
