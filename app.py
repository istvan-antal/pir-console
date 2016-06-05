#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pin_number=7

GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def motion_sense(channel):
    if GPIO.input(pin_number):
        print "Motion detected"

GPIO.add_event_detect(pin_number, GPIO.BOTH, callback=motion_sense, bouncetime=300)