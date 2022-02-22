from PIL import Image
import numpy as np
import time

img = Image.open("test-input-1.jpeg")

imgarr = np.asarray(img)

# check if approximations already exists

# linea
# r algorithm

start = time.time()
rows = []

for row in imgarr:
    counter = 0
    pointer1 = 0
    pointer2 = 0
    pointer1Calc = True
    for col in row:
        if pointer1Calc:
            if sum(col) > 675:
                counter += 1
            else:
                pointer1Calc = False
                pointer1 = counter
        else:
            if sum(col) < 675:
                counter += 1
            else:
                pointer2 = counter
                break
    rows.append([str(pointer1),str(pointer2)])

temp = map(",".join,rows)
tbw = "\n".join(temp)

fresult = open("testProcess.txt","w")
fresult.write(tbw)
fresult.close()


print(rows)
end = time.time()
print(end-start)
input()

# binary algorithm
