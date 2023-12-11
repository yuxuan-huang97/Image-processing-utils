"""
Program to convert a jpg or png image file to ppm p3 format

Specify the image to be converted with -f [image path]
or
Specify the directory containing all the images to be converted with -d [directory]

The output will be written to the same directory as this python script

by Yuxuan Huang
"""


import argparse
import os
from PIL import Image
from pathlib import Path


'''Argument Parsing'''


def parseArg():
    
    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-f", "--file", required=False,
       help="file to be converted")
    ap.add_argument("-d", "--directory", required=False,
       help="directory to be converted")
    return vars(ap.parse_args())

def toPPM(filename):
    img = Image.open(filename).convert('RGB')
    width = img.size[0]
    height = img.size[1]

    f = open(Path(filename).stem + ".ppm", "w")
    f.write("P3 " + str(width) + " " + str(height) + " " + str(255) + "\n")
    for r in range(0,height):
        for c in range(0,width):
            color = img.getpixel((c,r))
            for i in [0, 1, 2]:
                f.write(str(color[i]) + " ")
            f.write(" ")
        f.write("\n")
    print(os.path.basename(filename) + ' converted into ascii ppm successfully')
    f.close()

if __name__=="__main__": 
    
    args = parseArg()
    
    if (args['file']): # convert a single image
        toPPM(args['file'])
    
    
    else: # convert an entire directory 
        if args['directory'] == None:
            directory = os.getcwd()
            print("No file or directory specified. Default to current directory.")
        else:
            directory = args['directory']
        file_list = os.listdir(directory)
        if directory[-1] != '/': directory += '/'
        for file in file_list:
            if file[-4:] == '.jpg' or file[-4:] == '.png':
                toPPM(directory + file)
        
        
    