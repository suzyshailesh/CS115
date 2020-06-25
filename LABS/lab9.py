# mandelbrot.py
# Lab 9
#
# Name: Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    result = 0
    for i in range(0,n):
        result = result + c
    return result

def update(c,n):
    z = 0
    for i in range(0,n):
        z = z**2 + c
    return z

def inMset(c, n):
    z = 0
    for i in range(0,n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
                
    # we looped through every image pixel; we now write the file
    image.saveFile()

'''If the line if col%10 == 0 and row%10 == 0: is changed to
if col%10 == 0 or row%10 == 0:, the image would change because the image
would be a grid instead of just dots'''

def scale(pix, pixelMax, floatMin, floatMax):
    return ((1.0*pix/pixelMax) * (floatMax-floatMin)) + floatMin

def mset(width, height):
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            if inMset( c, 25 ) == True:
                image.plotPoint(col, row)
                
    # we looped through every image pixel; we now write the file
    image.saveFile()
