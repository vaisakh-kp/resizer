#!/usr/bin/python
from PIL import Image
import os, sys
path = "/home/vaisakhbeypore/resizer/png/"
dirs = os.listdir( path )
count = 1
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize25 = im.resize((25,25), Image.ANTIALIAS)
            imResize50 = im.resize((50,50), Image.ANTIALIAS)
            imResize75 = im.resize((75,75), Image.ANTIALIAS)
            filename = os.path.splitext(item)[0]
            imResize25.save('/home/vaisakhbeypore/resizer/resized/'+ filename + '@1x.png', 'PNG', quality=100)
            imResize50.save('/home/vaisakhbeypore/resizer/resized/'+ filename + '@2x.png', 'PNG', quality=100)
            imResize75.save('/home/vaisakhbeypore/resizer/resized/'+ filename + '@3x.png', 'PNG', quality=100)
            print(count)
            count = count + 1
resize()

