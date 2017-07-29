import RPi.GPIO as GPIO
from time import sleep

import logging

class MotorController:

  pinUp1 = 11
  pinUp2 = 13 

  pinDown1 = 15
  pinDown2 = 19 

  @staticmethod
  def init():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MotorController.pinUp1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MotorController.pinUp2, GPIO.OUT, initial=GPIO.HIGH)

    GPIO.setup(MotorController.pinDown1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(MotorController.pinDown2, GPIO.OUT, initial=GPIO.HIGH)

    MotorController.halt()

  @staticmethod
  def cleanup():
    GPIO.cleanup()

  @staticmethod
  def energize_up():
    GPIO.output(MotorController.pinUp1, GPIO.LOW)
    GPIO.output(MotorController.pinUp2, GPIO.LOW)

  @staticmethod
  def energize_down():
    GPIO.output(MotorController.pinDown1, GPIO.LOW)
    GPIO.output(MotorController.pinDown2, GPIO.LOW)

  @staticmethod
  def halt():
    GPIO.output(MotorController.pinUp1, GPIO.HIGH)
    GPIO.output(MotorController.pinUp2, GPIO.HIGH)
    GPIO.output(MotorController.pinDown1, GPIO.HIGH)
    GPIO.output(MotorController.pinDown2, GPIO.HIGH)
