from piCamera import PiCamera
from pathlib import *

photoDir = Path("test_photos")
if not photoDir.exists():
    Path().mkdir("test_photos")

cam = PiCamera()
cam.capture(f"{photoDir}/testimage.jpg")
