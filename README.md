# 👋 Welcome to Cloud9's 2021 submission to Astro Pi: Mission Space Lab!
This repository contains the code we submitted to be run on the ISS, along with some of the code we intended to use for processing the data we collected. Unfortunately, the code ran with an unhandled exception, so we didn't end up collecting any data. Whilst testing, the code very occasionally threw a random error which we didn't understand but which went away the next time it was run - this may have been the cause of the error.

## 💭 Our aim
Understanding how location, altitude, land type and plant health affect cloud distribution.

## ⌨️ Our code
* [main.final.py](main.final.py) - This is the code that we submitted
  * This took photos and broke them up into separate 100\*100 px images (chunks).
  * These would have been processed to identify the whitest chunks, which would have been assumed to be cloud
  * We would have compared the cloud cover in each chunk to data gathered from datasets for that area of the world, as well as NDVI calculated from the image
### Files which got incorporated into main.final.py
* [main.py](main.py) - An early version of main.final.py
* [capture_image.py](capture_image.py) - Takes photos
* [add_location.py](add_location.py) - Writes the current time and location to a specified text file
* [image_slicing.py](image_slicing.py) - Slices an image into multiple 100 by 100 chunks and discards chunks that are completely black

### Files which would have been used for post processing
* [ndvi.py](ndvi.py) - Creates NDVI images from the images it is input
* [average_rgb.py](average_rgb.py) - Gets the average RGB value of an image - would be used here to determine the average NDVI value of each chunk
* [pixel_classification.py](pixel_classification.py) - Returns the percentage of pixels in an image with RGB values above a specified threshold as a float -  would be used here to determine the brightness of an image to determine percentage cloud cover.
