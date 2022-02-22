from PIL import Image
import numpy as np

def slice(imgarr,width,height,indwidth,indheight,blackthreshold=20):
    for row in range(0,height,indheight):
        for col in range(0,width,indwidth):
            new_chunk = imgarr[row:row+indheight,col:col+indwidth]
            new_chunk_img = Image.fromarray(new_chunk)
            if np.average(new_chunk) <= blackthreshold: continue
            new_chunk_img.save(f"test_slice/chunk({row//indheight},{col//indwidth}).jpeg")

if __name__ == "__main__":
    img = Image.open("test-input-1.jpeg")
    width, height = img.size
    imgarr = np.asarray(img)

    indwidth = 100
    indheight = 100

    slice(imgarr,width,height,indwidth,indheight,20)