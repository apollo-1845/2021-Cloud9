from PIL import Image
import numpy as np

def slice(filepath,indwidth,indheight,blackthreshold=20):
    img = Image.open(f"{filepath}/unslicedPhoto.jpeg")
    width, height = img.size
    imgarr = np.asarray(img)
    for row in range(0,height,indheight):
        for col in range(0,width,indwidth):
            new_chunk = imgarr[row:row+indheight,col:col+indwidth]
            new_chunk_img = Image.fromarray(new_chunk)
            if np.average(new_chunk) <= blackthreshold: continue
            new_chunk_img.save(f"{filepath}/chunk({row//indheight},{col//indwidth}).jpeg")
