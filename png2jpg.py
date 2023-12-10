# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:33:32 2023

@author: Yuxuan Huang
"""

import os
from PIL import Image

img_path = "C:/Users/Yuxuan Huang/Desktop/temp figures"

# list all the files in the current directory
img_list = os.listdir(img_path)

# process all files
for img in img_list:
    if img[-3:] == 'png':
        # read img
        im = Image.open(img_path + "/" + img).convert('RGB')
        # resize img
        im = im.resize((1920, 1080))
        # convert img
        im.save(img[:-3] + 'jpg')
        print(img + " converted successfully")
        