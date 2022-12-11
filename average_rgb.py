import numpy as np
def main(image):
    print(image)
    print(np.average(image))

if __name__ == "__main__":
    from PIL import Image
    try:
        img = Image.open("test_slice\chunk(0,0).jpeg")
        main(np.asarray(img))
    except Exception as e:
        print(e)
    input()