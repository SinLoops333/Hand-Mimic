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
#2751.75
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_R3_up(self,value):
        kit.servo[0].set_pulse_width_range(1, 2750)
        time.sleep(0.01)
        kit.servo[0].angle = - value/182.05
        
    def on_R3_down(self,value):
        kit.servo[0].set_pulse_width_range(1, 2750)
        time.sleep(0.01)
        kit.servo[0].angle =  value/182.05          
    
        

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)