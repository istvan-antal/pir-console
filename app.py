#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
from csv import CSVFile

csv_file = CSVFile("stats.csv", ['time'])

GPIO.setmode(GPIO.BOARD)

pin_number=7

GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def motion_sense(pir_pin):
    print str(datetime.datetime.utcnow()) +  " Motion detected"
    csv_file.add_row([str(time.time())])

try:
    GPIO.add_event_detect(pin_number, GPIO.RISING, callback=motion_sense)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()