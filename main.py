from image_slicing import *
# from ndvi import *
# from ImageCaptureTest import *
from pathlib import *
import time


# setting up photo directory

photoDestination = Path("./CapturedImages")
if not photoDestination.exists():
    photoDestination.mkdir()

counter = 0
stopwatch = 5

previous = time.time()

# iteration

while counter < 10:
    current = time.time()
    if current - previous <= 4: continue
    else:
        previous = current
    photoPath = Path(f"./CapturedImages/Image{counter}")
    if not photoPath.exists():
        photoPath.mkdir()
    elif photoPath.stat().st_size == 0:
        counter += 1

    # originalImage = Path(take_pic(photoPath))

    oImage = Image.open(f"./Sample_Images/cslab3ogel_Files_RawData_raw_image_{counter + 1}.jpeg")
    originalImage = f"{photoPath}/unslicedPhoto.jpeg"
    oImage.save(originalImage)

    slice(photoPath,100,100,30)

    Path(originalImage).unlink()

    counter += 1
    print(f"Photo {counter} done")
