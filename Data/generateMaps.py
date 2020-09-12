'''
Authors : Amit Mishra, Pranath Reddy

Generates the maps from the input cl_data.fits 
'''

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")
print("by Pranath Reddy & Amit Mishra\n")
print("TEMPERATURE SKY MAP GENERATOR (Outputs file in standard fits format.)\n")

import healpy as hp
import numpy as np
import random
import time
import os
import math
import datetime

if not os.path.exists("./map_files"):
    os.makedirs("./map_files")

clsData = hp.read_cl('cl_data.fits')

nside = 1024

print("Enter the number of maps you want to generate:")
mapsToGenerate = input() #number of maps to generate

iterTime=0

Data_Labels = np.zeros(shape=(mapsToGenerate*12,1))
j = 0

while iterTime<mapsToGenerate :
    
    print("Generating map in fits format: "+str(iterTime+1)+"/"+str(mapsToGenerate))

    rint = random.randint(1000,3000)
    batchno = 1  # batch number if you want to generate maps in different batches
    np.random.seed(rint)

    timeNow = str(time.time()).split('.')[0]+str(batchno)

    file_name = str("./map_files/"+"mapv1-"+timeNow+".fits")

    createMap = hp.sphtfunc.synfast(cls=clsData, nside=nside)
    hp.write_map(file_name,createMap)

    alm = hp.sphtfunc.map2alm(createMap) 
    cl = hp.sphtfunc.alm2cl(alm)

    i=0
    x = np.linspace(0,len(cl[i]),len(cl[i]))

    y = np.zeros(len(cl[i]))

    # l*(l+1)*cl/2*pi is the y axis of power spectrum ( check notes )

    for l in range(1, len(cl[i])+1) :
        var = (l*(l+1)*cl[i][l-1])/2*math.pi
        y[l-1] = var
        
    # Matter density
    z = np.zeros(200)
    q = 0
    for k in range(400, 600) :
        z[q] = y[k]
        q += 1
        
    omega = (np.sort(z)[len(z)-1]/np.sort(y)[len(y)-1])/10
    #print(omega)

    k = j
    while(k<j+12) :
        Data_Labels[k] = omega
        k += 1 
    
   
    j += 12


    iterTime+=1
    print(datetime.datetime.now().time())

    
csvName = "Data_Labels-"+str(time.time()).split('.')[0]+".csv"
s = np.shape(Data_Labels)
print str(s)
np.savetxt(csvName, Data_Labels, delimiter=",")

print("Finished OK.")


