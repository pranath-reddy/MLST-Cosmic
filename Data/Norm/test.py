# Authors : Pranath Reddy, Amit Mishra

print("  _________ _____________  (_)____")
print("/ ___/ __ \/ ___/ __ `__ \/ / ___/")
print("/ /__/ /_/ (__  ) / / / / / / /__  ")
print("\___/\____/____/_/ /_/ /_/_/\___/ ")

print("A set of deep learning experiments on Cosmic Microwave Background Radiation Data")

import cv2
import matplotlib.pyplot as plt
import numpy as np
 
image = cv2.imread('test.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

holder = []
i = 0
j = 0

while j < gray[:,0].size:
    for i in range(0,gray[0,:].size):
        if gray[j][i] != 255:
            holder.append(gray[j][i])
    j = j + 1

holder = np.asarray(holder)
holder_avg = np.average(holder)
holder_std = np.std(holder)
holder2 = np.random.normal(loc=holder_avg,scale=holder_std,size=holder.shape)

plt.hist(holder, bins='auto')
plt.hist(holder2, bins='auto',alpha = 0.5, lw=3)
plt.title("Distros")
plt.show()



