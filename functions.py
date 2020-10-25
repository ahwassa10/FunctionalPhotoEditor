# Contains all the functions that be applied to the pixels of an image
# Saturday, October 24, 2020

# Example function
def dummy(pixel):
    """
    This is an example function.
    
    A filter function must be able to accept a 3-tuple as its first argument. 
    All other arguments must be optional.
    """
    dummy.args = []
    return pixel

def invert(pixel, channel=["R", "G", "B"]):
    invers.args = [["R", 0, 0], ["G", 0, 0], ["B", 0, 0]]
    tempPixel = []
    if "R" in channel:
        tempPixel[0] = 256 - i 
    else:
        tempPixel[0] = i
    
    if "G" in channel:
        tempPixel[1] = 256 - i 
    else:
        tempPixel[1] = i
    
    if "B" in channel:
        tempPixel[2] = 256 - i 
    else:
        tempPixel[2] = i 
    
    return tuple(tempPixel)