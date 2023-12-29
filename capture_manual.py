from time import sleep
import time
import picamera.array
from picamera import PiCamera
from imageio import imread
import numpy as np
import matplotlib.pyplot as plt
from keyboard import read_key

camera = PiCamera()
camera.rotation = 180
camera.contrast = 20
camera.brightness = 50
camera.framerate = 90 
camera.sensor_mode = 3
#camera.resolution = '1360x100'

sleep(2)

t = time.time()
output = picamera.array.PiRGBArray(camera)
camera.capture(output , 'rgb', use_video_port = False)
image = output.array
output.truncate(0)

print(time.time() - t)
plt.imshow(image)
plt.show()



