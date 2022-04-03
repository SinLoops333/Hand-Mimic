import board
import busio
import time
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import adafruit_motor.servo
#servo = adafruit_motor.servo.Servo()

#servokit.servo[0].actuation_range = 160

#MG995 Servo 180
pca.frequency = 25
kit.servo[0].set_pulse_width_range(400, 2430)
kit.servo[0].angle = 180
time.sleep(.85)
kit.servo[0].angle = 0

#9g Servo 180
kit.servo[1].set_pulse_width_range(420, 2415)
kit.servo[1].angle = 0
time.sleep(.5)
kit.servo[1].angle = 180

kit.continuous_servo[2].throttle = 1
time.sleep(1)
kit.continuous_servo[2].throttle = -1
time.sleep(1)
kit.continuous_servo[2].throttle = 0