# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:34:59 2023
autoConverter script to batch convert ascii ppm images into jpg
for csci 5607
@author: Yuxuan Huang
"""

import os
import PIL

answer_path = "../Answer/hw1d" # path to the folder containing sample images
submission_path = '../Grading' # path to the root folder containing all student submissions
image_names = ["Test1", "Test2", "Test3","Test4", "Test5", "Test6"] # names of the ppm images to be compared

# function to read the rgb values from ppm to a list
def readppm(path):
    if os.path.exists(path):
        file = open(path, "r").read()
        index = file.find("255") + 3 # find the starting index of the rgb values
        file = file[index:] # remove the header
        data = file.split() # store the rgb values into a list
        return data
    else:
        print(path + " does not exist")
        return []

# function to read ppm dimensions
def readppmDim(path):
    if os.path.exists(path):
        dim = []
        file = open(path, "r")
        Lines = file.readlines()
        for line in Lines:
            if line[0] == "#":
                continue
            else: 
                content = line.split()
                dim = dim + content
                    
            if len(dim) >= 3: # header, width and height
                break
                
        return int(dim[1]), int(dim[2])
    else:
        print(path + " does not exist")
        return -1, -1


# function to convert a ppm image to jpg and export to the same folder
def convertImage(path):
    width, height = readppmDim(path + ".ppm")
    if width < 0 or height < 0:
        return False
    img = readppm(path + ".ppm")
    jpgimg = PIL.Image.new(mode="RGB", size=(width, height))
    pixels = jpgimg.load()
    for i in range(height):
        for j in range(width):
            index = 3 * (i*width + j)
            pixels[j, i] = (int(float(img[index])), int(float(img[index+1])), int(float(img[index+2])))
    jpgimg.save(path + ".jpg")
    return True


if __name__ == "__main__":
    
    
    for img in image_names:
        if convertImage(answer_path + "/" + img):
            print(img + " - completed")
        else:
            print(img + " - failed")
    '''
    
    for root, dirs, files in os.walk(submission_path): # per student
        
        if root == submission_path: continue # skips the root dir
        print("\nConverting images for " + root)
        for img in image_names:
            if convertImage(root + "/" + img):
                print(img + " - completed")
            else:
                print(img + " - failed")
    
    '''
    