#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BOARD)

pin_number=7

GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def motion_sense(pir_pin):
    print datetime.datetime.utcnow() +  " Motion detected"

try:
    GPIO.add_event_detect(pin_number, GPIO.RISING, callback=motion_sense)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()