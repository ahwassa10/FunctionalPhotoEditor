# Functional Photo Editor
# Saturday, October 22, 2020

from PIL import Image

def dummy(pixel):
    return pixel

def applyFilter(image, function=dummy):
    data = []
    for pixel in image.getdata():
        data.append(function(pixel))
    
    copiedImage = Image.new("RGB", image.size)
    copiedImage.putdata(data)
    copiedImage.show()

testImage = Image.open("test3.bmp") 
applyFilter(testImage)