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
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import math

print("Importing the Data")
x_train = np.load('x_train_cmb.npy')
x_test = np.load('x_test_cmb.npy')
y_train = np.load('y_train_cmb.npy')
y_test = np.load('y_test_cmb.npy')

model = Sequential()
model.add(Conv1D(filters=64, kernel_size=(32), input_shape=(4096,1), strides=2, padding='valid', activation='relu'))
model.add(AveragePooling1D(pool_size=2,strides=2,padding='same'))
model.add(Conv1D(filters=32, kernel_size=(32), strides=2, padding='valid', activation='relu'))
model.add(AveragePooling1D(pool_size=2, strides=2, padding='same'))
model.add(Conv1D(filters=16, kernel_size=(32), strides=2, padding='valid', activation='relu'))
model.add(AveragePooling1D(pool_size=2, strides=2, padding='same'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

#model = load_model('CMB_CNN_100.h5')
#print('model loaded')

model.compile(loss='mean_absolute_error', optimizer=Adam(lr=1e-3, decay=1e-5))
model_history=model.fit(x_train, y_train, batch_size=512, epochs=100)
model.summary()

model.save('CMB_CNN_100.h5')
print('model saved')

plt.plot(model_history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

y_pred = model.predict(x_test)

print(y_pred)
print(y_test)
    
print('MAE:')
print(mean_absolute_error(y_test, y_pred))
print('RMSE:')
print(math.sqrt(mean_squared_error(y_test, y_pred)))

def Average(lst):
    return sum(lst) / len(lst)
    
error = [0 for i in range(len(y_test.shape))]
for i in range(len(y_test.shape)):
    error[i] = abs((y_test[i]-y_pred[i])/y_test[i])
    
print('MRE:')
print(Average(error))





