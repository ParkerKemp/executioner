#!/usr/bin/env python

import RPi.GPIO as GPIO
from configuration import DoorStatus

import logging

class SwitchController:

    statusPin = 16

    @staticmethod
    def init():
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(SwitchController.statusPin, GPIO.IN)

    @staticmethod
    def get_status():
        if(GPIO.input(SwitchController.statusPin)):
            return DoorStatus.Closed
        else:
            return DoorStatus.Open

