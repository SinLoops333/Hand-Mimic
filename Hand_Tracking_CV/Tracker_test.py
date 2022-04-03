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

    def on_R3_up(self,value):
        kit.servo[0].set_pulse_width_range(10, 2750)
        time.sleep(0.01)
        kit.servo[0].angle = - value/182.05
        
    def on_R3_down(self,value):
        kit.servo[0].set_pulse_width_range(10, 2750)
        time.sleep(0.01)
        kit.servo[0].angle =  value/182.05
        
  
        

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen(timeout=60)

# res = tuple(map(lambda i, j: i - j, pixelCoordinatesLandmark, pixelCoordinatesLandmark1))
#                       res1 = tuple(map(lambda i, j: i - j, pixelCoordinatesLandmark, pixelCoordinatesLandmark1))
#                       print(res)
#                       print(res1)
#                       if type(pixelCoordinatesLandmark) != type(None) and type(pixelCoordinatesLandmark1) != type(None):
#                           d = math.sqrt((abs(pixelCoordinatesLandmark1[0] - pixelCoordinatesLandmark[0]))^2 + (abs(pixelCoordinatesLandmark1[1] - pixelCoordinatesLandmark[1]))^2)
#                           print(d)
         

#                       normalizedLandmark2 = handLandmarks.landmark[5]
#                       pixelCoordinatesLandmark2= drawingModule._normalized_to_pixel_coordinates(normalizedLandmark2.x, normalizedLandmark2.y, 640, 480)
#                       print(pixelCoordinatesLandmark2)

#                       if type(pixelCoordinatesLandmark) != type(None) and type(pixelCoordinatesLandmark1) != type(None):
#                           res = tuple(map(lambda i, j: i - j, pixelCoordinatesLandmark, pixelCoordinatesLandmark1))
#                          # res1 = tuple(map(lambda i, j: i - j, pixelCoordinatesLandmark, pixelCoordinatesLandmark1))
#                           print(res)
                        #  print(res1)