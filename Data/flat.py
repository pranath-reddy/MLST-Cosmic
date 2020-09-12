'''
Authors : Amit Mishra, Pranath Reddy
'''
'''
Flattens the cropped images and exports the data into a csv file
(Used for tensorflow implementation)
'''

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")
print("by Pranath Reddy & Amit Mishra\n")
print("CONVERT IMAGE INTO CSV FILE (Outputs file CSV format.)\n")

import cv2
import numpy as np
import os

# Put the cropped images in the same directory as this one
mypath = './cropped_files'
files = [os.path.join(mypath, f) for f in os.listdir(mypath) if f.endswith(".png")]

numOfImages = len(files)

final = np.zeros(shape=(numOfImages,4096))

i=0

for images in files:
    image = cv2.imread(images,0) 
    data = np.array(image)
    flattened = data.flatten()
    final[i] = flattened
    i = i+1

s = np.shape(final)
print str(s)
np.savetxt("Data.csv", final, delimiter=",")
print(final)
