# Authors : Pranath Reddy, Amit Mishra

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")

import numpy as np
import os
import h5py
import pandas as pd

data = pd.read_csv('./Data.csv',header=None)
x = data.iloc[:,:].values
print("imported")

x = x.astype(np.uint8)

print("converted")

with h5py.File('Data.h5', 'w') as hf:
    hf.create_dataset("data",  data=x)

print(x)
print(x.shape)

print("done")
