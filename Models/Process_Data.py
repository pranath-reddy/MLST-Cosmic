# Authors : Pranath Reddy, Amit Mishra

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")

import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Activation, UpSampling2D, Flatten, Reshape, BatchNormalization, LSTM, Bidirectional,Conv1D,AveragePooling1D,Flatten
from keras.utils import *
from keras.optimizers import *
import keras.backend as K
from keras.models import load_model
from sklearn.model_selection import train_test_split

print("Importing the Data")

with h5py.File('Data.h5', 'r') as hf:
    x = hf['data'][:]
    
print('Shape of features:', x.shape)

labels = pd.read_csv('./Labels.csv',header=None)
labels.drop([0],axis=1)

y = labels.iloc[:,:].values.flatten()
print('Shape of Labels:', y.shape)

y = np.asmatrix(y)
y = y.T
y = np.asarray(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train = x_train.reshape(-1,4096,1)
x_test = x_test.reshape(-1,4096,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

np.save('x_train_cmb.npy',x_train)
np.save('x_test_cmb.npy',x_test)
np.save('y_train_cmb.npy',y_train)
np.save('y_test_cmb.npy',y_test)


