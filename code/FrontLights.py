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

def Both_on():
    GPIO.output(left_R, on)
    GPIO.output(left_G, on)
    GPIO.output(left_B, on)

    GPIO.output(right_R, on)
    GPIO.output(right_G, on)
    GPIO.output(right_B, on)

def Setup():#initialization
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_R, GPIO.OUT)
    GPIO.setup(left_G, GPIO.OUT)
    GPIO.setup(left_B, GPIO.OUT)
    GPIO.setup(right_R, GPIO.OUT)
    GPIO.setup(right_G, GPIO.OUT)
    GPIO.setup(right_B, GPIO.OUT)
    Both_off()

def Both_off():
    GPIO.output(left_R, off)
    GPIO.output(left_G, off)
    GPIO.output(left_B, off)

    GPIO.output(right_R, off)
    GPIO.output(right_G, off)
    GPIO.output(right_B, off)
    
def ColorRed():
    GPIO.output(left_R, on)
    GPIO.output(left_G, off)
    GPIO.output(left_B, off)

    GPIO.output(right_R, on)
    GPIO.output(right_G, off)
    GPIO.output(right_B, off)

def ColorGreen():
    GPIO.output(left_R, off)
    GPIO.output(left_G, on)
    GPIO.output(left_B, off)

    GPIO.output(right_R, off)
    GPIO.output(right_G, on)
    GPIO.output(right_B, off)