import sys, tty, termios, time
import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import adafruit_motor.servo
from pyPS4Controller.controller import Controller


def konami_callback():
    print("Konami sequence detected!")


def my_sequences():
    return [
        {"inputs": ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'share', 'options'],
         "callback": konami_callback}
    ]


controller = Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(on_sequence=my_sequences())

class MyController(Controller):


    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.step = 1
        self.pwm = adafruit_pca9685.PCA9685()
        self.command = False

    def on_x_press(self):
        self.command = True
        while self.command == True:
            move(self.step, 35, 'forward')
            self.step +=1
            if self.step > 4:
                self.step = 1
            time.sleep(0.08)

    def on_x_release(self):
        self.command = False



