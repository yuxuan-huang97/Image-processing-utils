"""
Program to convert an image file to ppm p3 format
by Yuxuan Huang
"""

import cv2

filename = "impressionsunrise"
fileformat = "jpg"

img = cv2.imread(filename+'.'+fileformat, flags=cv2.IMREAD_COLOR)
height = img.shape[0]
width = img.shape[1]

f = open(filename+".ppm", "w")
f.write("P3 " + str(width) + " " + str(height) + " " + str(255) + "\n")
for r in range(0,height):
    for c in range(0,width):
        for i in [2, 1, 0]:
            #f.write(str(img[r][width-c-1][i]) + " ")
            f.write(str(img[r][c][i]) + " ")
        f.write(" ")
    f.write("\n")
f.close()
