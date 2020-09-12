# Authors : Pranath Reddy, Amit Mishra

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")

import pandas as pd
import numpy as np

i = 0
j = 0
data = pd.read_csv('./Data.csv',header=None)
x = data.iloc[1:,1:].values
while j < x[:,0].size:
    for i in range(0,x[0,:].size):
        if x[j][i] < 112 or x[j][i] > 131:
                x[j][i] = 0
    j = j + 1

np.savetxt("nData.csv", x, delimiter=",")
