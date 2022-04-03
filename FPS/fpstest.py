from threading import Thread
import cv2
import numpy as np
import imutils
 
src='rtsp://web_camera_ip'
stream_in = WebcamVideoStream(src).start()
pipeline_out = "appsrc ! videoconvert ! video/x-raw, framerate=20/1, format=RGBA ! glimagesink sync=false"
fourcc = cv2.VideoWriter_fourcc(*'H264')
 
stream_out = cv2.VideoWriter(pipeline_out, cv2.CAP_GSTREAMER, fourcc, 20.0, (1280,720))
while True:
    frame = stream_in.read()
    out.write(frame)
    cv2.waitKey(1)