from picamera import PiCamera
from pathlib import *

def take_pic(filepath):
    cam = PiCamera()
    cam.capture(f"{filepath}/unslicedPhoto.jpeg")

    # log stuff

    return Path(f"{filepath}/unslicedPhoto.jpeg")
