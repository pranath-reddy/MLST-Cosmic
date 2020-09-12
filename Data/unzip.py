# Authors : Pranath Reddy, Amit Mishra

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")

import numpy as np
import pandas as pd
import os
import cv2

if not os.path.exists("./testimages"):
    os.makedirs("./testimages")

data = pd.read_csv('./TData.csv',header=None)

x = data.iloc[1:,1:].values
y = np.zeros((1200,64,64))

for i in range(0,1200):
    y[i] = x[i].reshape(64,64)
    cv2.imwrite('./testimages/' + str(i) + '.png',y[i])

