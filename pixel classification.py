import numpy as np

def pixel_classification(image_array,total_pixels,rmin,rmax,gmin,gmax,bmin,bmax):
    """takes in image as numpy array, returns percentage of pixels within certain colour range as a float value"""
    colour_count = 0
    for x in image_array:
        for y in x:
            if y[0] >= rmin and y[0] <= rmax:
                if y[1] >= gmin and y[1] <= gmax:
                    if y[2] >= bmin and y[1] <= bmax:
                        colour_count += 1
    return colour_count/total_pixels


rgb_range = np.array([[150,200],[180,255],[200,255]]) #[rmin,rmax],[gmin,gmax],[bmin,bmax]