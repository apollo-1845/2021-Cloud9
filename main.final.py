from pathlib import Path
from orbit import ISS
from skyfield.api import load 
from PIL import Image
import numpy as np
from picamera import PiCamera
from datetime import datetime, timedelta
from logzero import logger, logfile
import time

def slice(filepath,indwidth,indheight,blackthreshold=25):

    # This function slices an image into multiple 100 by 100 chunks
    img = Image.open(f"{filepath}/unslicedPhoto.jpeg")
    width, height = img.size
    imgarr = np.asarray(img)

    for row in range(0,height,indheight):
        for col in range(0,width,indwidth):
            new_chunk = imgarr[row:row+indheight,col:col+indwidth]
            new_chunk_img = Image.fromarray(new_chunk)

            # This discards chunks that are completely black (e.g. the outer rim) to save storage space
            if np.average(new_chunk) <= blackthreshold: continue 
            
            # The file name is saved in a way that its relative coordinates are in the file name
            # So if the image is to be reassembled, it can be done by reading the file name
            new_chunk_img.save(f"{filepath}/chunk({row//indheight},{col//indwidth}).jpeg")

def take_pic(filepath):
    cam = PiCamera()
    cam.capture(f"{filepath}/unslicedPhoto.jpeg") 
    cam.close()
    # This photo needs to be deleted (to save storage space) so the file path is returned
    return Path(f"{filepath}/unslicedPhoto.jpeg")

def add_location(output):
    ''' Writes the current time and location to a specified text file'''
    # Obtain the current time `t`
    t = load.timescale().now()
    # Compute where the ISS is at time `t`
    position = ISS.at(t)
    # Compute the coordinates of the Earth location directly beneath the ISS
    location = position.subpoint()

    file = open(output, 'w')
    file.writelines(str(location))
    file.writelines(str(datetime.now()))
    file.close()


if __name__ == "__main__":

    storage = 0

    # Stores all photos in "CapturedImages"
    photoDestination = Path("./CapturedImages")
    if not photoDestination.exists():
        photoDestination.mkdir()

    # creates logger file to check     
    logfile("./events.log")

    # Used so that each file name is unique
    counter = 1 

    # Count the time
    start_time = datetime.now()
    now_time = datetime.now()

    while (now_time < start_time + timedelta(minutes = 179)): 

        try:       
            photoPath = Path(f"./CapturedImages/Image{counter}")
            if not photoPath.exists():
                photoPath.mkdir() # Creates a new directory for each image
            
            originalImage = take_pic(photoPath) # Takes image and saves the path

            # splits it into 100 x 100 chunks and discarding chunks with average RGB values below 25
            slice(photoPath,100,100,25)

            originalImage.unlink() # Deletes original unsliced image

            add_location(f"{photoPath}/data.txt") # logs the time and location

            counter += 1

            # keeps track of the file size
            for file in photoPath.iterdir():
                storage += file.stat().st_size
             
            # terminates before file size is too big             
            if storage > 3150000000:
                break
            
            time.sleep(1) # Add some delay before taking another picture
            
        except Exception as e:
            try: # just in case the logger doesn't work
                logger.error(f"{e.__class__.__name__}: {e}")
            except:
                pass
    