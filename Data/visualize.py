'''
Authors : Amit Mishra, Pranath Reddy

Exports the map images from the generated .fits files from generateMaps.py 
'''

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")
print("FITS TO PNG CONVERTER (Outputs image in PNG format. MollView Projection)\n")

import healpy as hp 
import numpy as np 
import matplotlib.pyplot as plt
import os

if not os.path.exists("./image_files"):
    os.makedirs("./image_files")

mapFiles = []
for dirname, dirnames, filenames in os.walk('./map_files/'):
    for filename in filenames:
        mapFiles.append(os.path.join(dirname, filename))


print("Do you want image with equator along the center?(y/n)")
ans = raw_input()

if ans == "y" or ans == "Y" or ans == "":
    for i in range(len(mapFiles)):
    
        print("\nProcessing: "+mapFiles[i])
        
        imageName = mapFiles[i].split("/")[2].split(".")[0]+".png"
        mapData = hp.read_map(mapFiles[i])
        hp.mollview(mapData,title="",notext="true",xsize=4096,cbar="None",max=0.00045)
        os.chdir('./image_files')
        plt.savefig(imageName)
        os.chdir('../')
        print("Generated map image : "+str(i+1)+"/"+str(len(mapFiles)))
        
        # clear image from memory
        plt.clf()

elif ans == "n" or ans == "N":
    print("Enter longitude which will be at the center:")
    lon = raw_input()
    print("Enter latitude which will be at the center:")
    lat = raw_input()
    print("Enter angle to be rotated at:")
    psi = raw_input()

    for i in range(len(mapFiles)):
    
        print("\nProcessing: "+mapFiles[i])
        
        imageName = mapFiles[i].split("/")[2].split(".")[0]+".png"
        mapData = hp.read_map(mapFiles[i])
        hp.mollview(mapData,rot=(lon,lat,psi),title="",notext="true",xsize=4096,cbar="None",max=0.00045)
        os.chdir('./image_files')
        plt.savefig(imageName)
        os.chdir('../')
        print("Generated map image : "+str(i+1)+"/"+str(len(mapFiles)))
        
        # clear image from memory
        plt.clf()

else:
    print("Invalid input. Exiting.")


print("\nFinished")
