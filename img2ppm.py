"""
Program to convert an image file to ppm p3 format
by Yuxuan Huang
"""

from PIL import Image

filename = "brick_wall_nor"
fileformat = "jpg"

img = Image.open(filename+'.'+fileformat).convert('RGB')
height = img.size[0]
width = img.size[1]

f = open(filename+".ppm", "w")
f.write("P3 " + str(width) + " " + str(height) + " " + str(255) + "\n")
for r in range(0,height):
    for c in range(0,width):
        color = img.getpixel((c,r))
        for i in [0, 1, 2]:
            f.write(str(color[i]) + " ")
        f.write(" ")
    f.write("\n")
f.close()