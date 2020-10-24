# Image Testing
# Saturday, October 24, 2020
from PIL import Image
import random

def test1():
    testImage = Image.open("test.bmp")
    
    #Format is the file format, size is 2 tuple storing width and height in pixels, mode is "RGB"
    #Prints out BMP (2064, 864) RGB
    print(testImage.format, testImage.size, testImage.mode)
    
    testImage.show()

def test2():
    testImage = Image.open("test2.bmp")
    
    def invert(i):
        return 256-i 
    
    def double(i):
        i = i * 2
        if i > 256:
            i = i - 256
        return i
    
    nImage = Image.eval(testImage, double)
    nImage.show()

def test3():
    testImage = Image.open("test2.bmp")
    
    rChannel = testImage.getchannel(0)
    gChannel = testImage.getchannel(1)
    bChannel = testImage.getchannel(2)
    
    rChannel.show()
    gChannel.show()
    bChannel.show()
    
def test4():
    testImage = Image.open("test2.bmp")
    
    testPixel = testImage.getpixel((0,0))
    print (testPixel)

def test5():
    testImage = Image.open("test2.bmp")
    for i in range(testImage.size[0]):
        for j in range(testImage.size[1]):
            tempPixel = testImage.getpixel((i, j))
            k = random.randint(0, 100)
            tempPixel = (min(256, tempPixel[0]+k), tempPixel[1], tempPixel[2])
            testImage.putpixel((i,j), tempPixel)
    testImage.show()

test5()