import cv2
import numpy as np

def contrast_stretch(im):
    '''Increases contrast on an image - copied from RPi Learning'''
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

def calc_ndvi(image):
    ''' Calculates NDVI values - copied from RPi Learning'''
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    ndvi = (b.astype(float) - r) / bottom
    return ndvi

def convert_to_ndvi(original_file_path, output_name):
    '''Converts a named file to an NDVI image'''
    original = cv2.imread(original_file_path)
    contrasted = contrast_stretch(original)
    #cv2.imwrite('contrasted.png', contrasted)
    ndvi = calc_ndvi(contrasted)
    ndvi = contrast_stretch(ndvi)
    cv2.imwrite(output_name, ndvi)


if __name__ == "__main__":
    convert_to_ndvi("test-input-1.jpeg", "ndvi.jpeg")
