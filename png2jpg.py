# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:33:32 2023

Convert all png in a folder into jpg and optionally resize

-d [directory]
-r [height after resize]

The output will be written to the same directory as this python script

@author: Yuxuan Huang
"""

import argparse
import os
from PIL import Image
from pathlib import Path

def toPNG(img):
    img_name = Path(img).stem
    if img[-4:] == '.png':
        # read img
        im = Image.open(img).convert('RGB')
        # resize img
        if args['height']:
            new_h = int(args['height'])
            w = im.size[0]
            h = im.size[1]
            if new_h < h: # resize the image only if the new size is smaller
                new_w = int(w*new_h/h)
                im = im.resize((new_w, new_h))
                print("resizing to %d x %d"%(new_w, new_h))
        # convert img
        im.save(img_name + '.jpg')
        print(img_name + ".png converted to jpg successfully")
        
        
def parseArg():
    
    # Construct the argument parser
    ap = argparse.ArgumentParser()
    
    # Add the arguments to the parser
    ap.add_argument("-d", "--directory", required=False,
       help="directory to be converted")
    ap.add_argument("-r", "--height", required=False,
       help="height after resize")
    return vars(ap.parse_args())

if __name__=="__main__": 
    
    args = parseArg()
    
    if args['directory'] == None:
        directory = os.getcwd()
        print("No directory specified. Default to current directory.")
    else:
        directory = args['directory']
    file_list = os.listdir(directory)
    if directory[-1] != '/': directory += '/'
    for file in file_list:
        if file[-4:] == '.png':
            toPNG(directory + file)
        