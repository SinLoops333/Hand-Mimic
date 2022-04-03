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

class MyController(Controller):   
   
    def on_up_arrow_press(self):
        kit.servo[0].set_pulse_width_range(400, 2430)
        kit.servo[0].angle = 180
       # time.sleep(.5)
    def on_down_arrow_press(self):
        print("Retrun 2")
        kit.servo[0].set_pulse_width_range(400, 2430)
        kit.servo[0].angle = 0
       # time.sleep(.5)
    def on_left_arrow_press(self):
        kit.servo[1].set_pulse_width_range(400, 2430)
        kit.servo[1].angle = 180
       # time.sleep(.5)
    def on_right_arrow_press(self):
        print("Retrun 2")
        kit.servo[1].set_pulse_width_range(400, 2430)
        kit.servo[1].angle = 0
       # time.sleep(.5)
    def on_triangle_press(self):
        kit.servo[2].set_pulse_width_range(400, 2430)
        kit.servo[2].angle = 180
       # time.sleep(.5)
    def on_x_press(self):
        print("Retrun 2")
        kit.servo[2].set_pulse_width_range(400, 2430)
        kit.servo[2].angle = 0
       # time.sleep(.5)
    def on_square_press(self):
        kit.servo[3].set_pulse_width_range(400, 2430)
        kit.servo[3].angle = 180
       # time.sleep(.5)
    def on_circle_press(self):
        print("Retrun 2")
        kit.servo[3].set_pulse_width_range(400, 2430)
        kit.servo[3].angle = 0
       # time.sleep(.5)
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)