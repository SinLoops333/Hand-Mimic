import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
start = time.time()

for img in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    frame = img.array
    rawCapture.truncate(0)
    end = time.time()
    print ('fps:', int(round(1 / (end - start))))
    start = time.time()
