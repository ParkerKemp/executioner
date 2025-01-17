#!/usr/bin/env python

import RPi.GPIO as GPIO
from configuration import DoorStatus

import logging

class SwitchController:

    statusPin = 16

    @staticmethod
    def init():
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(SwitchController.statusPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @staticmethod
    def get_status():
        if(GPIO.input(SwitchController.statusPin)):
            return DoorStatus.Open
        else:
            return DoorStatus.Closed

