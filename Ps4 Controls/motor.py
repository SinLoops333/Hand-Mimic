import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import adafruit_motor.servo
from pyPS4Controller.controller import Controller
pca.frequency = 25
kit.servo[0].set_pulse_width_range(1, 2750)
kit.servo[0].angle = 180
time.sleep(0.01)
kit.servo[0].angle = 0
time.sleep(0.01)
kit.servo[0].angle = 180