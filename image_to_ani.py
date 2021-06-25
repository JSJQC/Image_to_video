# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 13:47:50 2021

@author: jakes


This code is geared towards being used with Ansys Fluent animation outputs
"""

import cv2
import os


image_folder = "" # This is the file the images are kept in -> needs the full file path

video_name = input("Enter the video name + extension: ") # Name of the file you will create

object_name = input("Enter the name of the graphic: ") # i.e. pressure_contours ...

number_of_snaps = int( input( "Enter the number of frames outputted by Fluent: ")) # how many timesteps essentially


images = []

for ending in range(number_of_snaps):
    
    padding_number = 4 - len(str(ending)) # This is to pad the zeroes in front of the number
    
    padded_number = ("0" * padding_number) + f"{ending}"
    
    image_name = object_name + "_1" + "_" + padded_number + ".jpg" ## The "_1" may not always be needed, checked the files themselves before running
    
    images.append(image_name)


frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width,height)) # '10' is the fps number, check documentation for more

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
