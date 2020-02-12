# -*- coding: utf-8 -*-
"""FisherDiscriminant5sand6s.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XoYUNkI-WJLZHpRaLSZVmbsJp9eOW-d6

## **Import packages**

## **Load and visualize MNIST da   t  a**
"""

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from skimage import measure

import warnings
warnings.filterwarnings("ignore") # Added this at the end to show a clean output with no warnings but not necessary

"""### Choose number to visualize (from 0 to 9):"""

(x_train, y_train), (x_test, y_test) = mnist.load_data()

number5 = 5
x_5 = x_train[y_train==number5,:,:]
print('The shape of 5 is:')
print(x_5.shape)
print('which means:')
print('Number '+str(number5)+' has '+str(x_5.shape[0])+' images of size '+str(x_5.shape[1])+'x'+str(x_5.shape[2]))

print()
number6 = 6
x_6 = x_train[y_train==number6,:,:]
print('The shape of 6 is:')
print(x_6.shape)
print('which means:')
print('Number '+str(number6)+' has '+str(x_6.shape[0])+' images of size '+str(x_6.shape[1])+'x'+str(x_6.shape[2]))

"""### Plot average image:"""

m5 = np.mean(x_5, axis=0) # IMPORTANT: indexes in python start at "0", not "1", so the first element of array "a" would be a[0]

plt.figure()
plt.subplot(2,2,1)
plt.imshow(m5)
plt.title('Average "5" image')

mt5 = 1*(m5 > 100) # Thresholding
plt.subplot(2,2,2)
plt.imshow(mt5)
plt.title('Thresholded "5" image')

m6 = np.mean(x_6, axis=0) # IMPORTANT: indexes in python start at "0", not "1", so the first element of array "a" would be a[0]

plt.figure()
plt.subplot(2,2,3)
plt.imshow(m6)
plt.title('Average "6" image')

mt6 = 1*(m6 > 100) # Thresholding
plt.subplot(2,2,4)
plt.imshow(mt6)
plt.title('Thresholded "6" image')

"""## From a thresholded image, we can use the regionprops function from skimage.measure"""

mt5_props = measure.regionprops(mt5)
num_regions = len(mt5_props)
print(str(num_regions)+' region/s were found. Handwritten 5s')
print('')

print('Area (in pixels):')
area = mt5_props[0].area # Remember, index 0 is the first region found
print(area)
print('')

print('Perimeter (in pixels):')
perimeter = mt5_props[0].perimeter
print(perimeter)
print('')

print('Centroid (pixel coordinates):')
centroid = mt5_props[0].centroid
print(centroid)

print('Eccentricity:')
eccentricity = mt5_props[0].eccentricity
print(eccentricity)
print('')

print('Minor axis length:')
minor_axis = mt5_props[0].minor_axis_length
print(minor_axis)
print('')

print('Convex Area:')
convex_area = mt5_props[0].convex_area
print(convex_area)
print('')

print('Major Axis Length:')
major_axis_length = mt5_props[0].major_axis_length
print(major_axis_length)
print('')

print('Euler Number:')
euler_number = mt5_props[0].euler_number
print(euler_number)
print('')

mt6_props = measure.regionprops(mt6)
num_regions = len(mt6_props)
print(str(num_regions)+' region/s were found. Handwritten 6s')
print('')

print('Area (in pixels):')
area = mt6_props[0].area # Remember, index 0 is the first region found
print(area)
print('')

print('Perimeter (in pixels):')
perimeter = mt6_props[0].perimeter
print(perimeter)
print('')

print('Centroid (pixel coordinates):')
centroid = mt6_props[0].centroid
print(centroid)

print('Eccentricity:')
eccentricity = mt6_props[0].eccentricity
print(eccentricity)
print('')

print('Minor axis length:')
minor_axis = mt6_props[0].minor_axis_length
print(minor_axis)
print('')

print('Convex Area:')
convex_area = mt6_props[0].convex_area
print(convex_area)
print('')

print('Major Axis Length:')
major_axis_length = mt6_props[0].major_axis_length
print(major_axis_length)
print('')

print('Euler Number:')
euler_number = mt6_props[0].euler_number
print(euler_number)
print('')

"""##Scatter plot of different features for all images of numbers "5" and "6""""

x5 = x_train[y_train==5,:,:]
x6 = x_train[y_train==6,:,:]

# Threshold images
t5 = 1*(x5 > 100)
t6 = 1*(x6 > 100)

# Region properties
euler5 = np.zeros(t5.shape[0])
eccentricity5 = np.zeros(t5.shape[0])
perimeter5 = np.zeros(t5.shape[0])
area5 = np.zeros(t5.shape[0])
major_axis_length5 = np.zeros(t5.shape[0])
for i in range(0,t5.shape[0]):
  props = measure.regionprops(t5[i,:,:])
  eccentricity5[i] = props[0].eccentricity
  perimeter5[i] = props[0].perimeter
  major_axis_length5[i] = props[0].major_axis_length
  euler5[i] = props[0].euler_number
  area5[i] = props[0].area
  
euler6 = np.zeros(t6.shape[0])
eccentricity6 = np.zeros(t6.shape[0])
perimeter6 = np.zeros(t6.shape[0])
major_axis_length6 = np.zeros(t6.shape[0])
area6 = np.zeros(t6.shape[0])
for i in range(0,t6.shape[0]):
  props = measure.regionprops(t6[i,:,:])
  eccentricity6[i] = props[0].eccentricity
  perimeter6[i] = props[0].perimeter
  major_axis_length6[i] = props[0].major_axis_length
  euler6[i] = props[0].euler_number
  area6[i] = props[0].area

plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
plt.scatter(major_axis_length5,area5, label='Number 5')
plt.scatter(major_axis_length6,area6, label='Number 6')
plt.title('All images for both classes')
plt.legend()

plt.subplot(1,2,2)
plt.scatter(major_axis_length5[0:100],euler5[0:100], label='Number 5')
plt.scatter(major_axis_length6[0:100],euler6[0:100], label='Number 6')
plt.title('100 images of each class')
plt.legend()

X5 = np.zeros((t5.shape[0],2))
for i in range(0,t5.shape[0]):
  X5[i] = [major_axis_length5[i],area5[i]]
  
X6 = np.zeros((t6.shape[0],2))
for i in range(0,t6.shape[0]):
  X6[i] = [major_axis_length6[i],area6[i]]

  
X = np.append(X5,X6,axis = 0)

print('0s class:\n', X5)
print('1s class:\n', X6)
print('Two classes together:\n', X)

#Mean Vectors

m5 = np.mean(X5, axis=0)
m6 = np.mean(X6, axis=0)

m_overall = np.mean(X, axis=0)

print('5s mean:\n', m5)
print('6s mean:\n', m6)
print('Overall mean:\n', m_overall)

#Scatter Matrix

  #Within-Class Scatter
  SW = np.zeros((2,2))
  
  for i in X5:
    i,m5 = i.reshape(2,1), m5.reshape(2,1)
    SW += (i-m5).dot((i-m5).T)

  for i in X6:
    i,m6 = i.reshape(2,1), m6.reshape(2,1)
    SW += (i-m6).dot((i-m6).T)
    
  print('Within-Class Scatter Matrix:\n', SW)
  
  #Between-Class Scatter
  SB = np.zeros((2,2))  
  m5,m6,m_overall = m5.reshape(2,1), m6.reshape(2,1), m_overall.reshape(2,1)
  SB = t5.shape[0]*(m5-m_overall).dot((m5-m_overall).T) + t6.shape[0]*(m6-m_overall).dot((m6-m_overall).T)
  
  print('Between-Class Scatter Matrix:\n', SB)

#Eigenvalues for scatter matrices
eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(SW).dot(SB))

for i in range(len(eig_vals)):
    eigvec_sc = eig_vecs[:,i].reshape(2,1)   
    print('\nEigenvector {}: \n{}'.format(i+1, eigvec_sc.real))
    print('Eigenvalue {:}: {:.2e}'.format(i+1, eig_vals[i].real))

# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues

print('Eigenvalues in decreasing order:\n')
for i in eig_pairs:
    print(i[0])

w = 1*np.hstack((eig_pairs[0][1].reshape(2,1)))
print('w:\n', w)

#Threshold calculation
T = (np.dot(w, m5)+np.dot(w, m6))*0.5
print(T)

fails = 0

for i in X5:
  if(np.dot(w, i) < T):     
     fails += 1

for i in X6:
  if(np.dot(w, i) > T):
     fails += 1

      
print('Accuracy: ',(1-(fails/X.shape[0]))*100)

x5test = x_test[y_test==5,:,:]
x6test = x_test[y_test==6,:,:]

# Threshold images
t5test = 1*(x5test > 60)
t6test = 1*(x6test > 60)

# Region properties
area5test = np.zeros(t5test.shape[0])
perimeter5test = np.zeros(t5test.shape[0])
major_axis_length5test = np.zeros(t5test.shape[0])
euler5test = np.zeros(t5test.shape[0])
area5test = np.zeros(t5test.shape[0])
for i in range(0,t5test.shape[0]):
  propstest = measure.regionprops(t5[i,:,:])
  area5test[i] = propstest[0].area
  perimeter5test[i] = propstest[0].perimeter
  major_axis_length5test[i] = propstest[0].major_axis_length
  euler5test[i] = propstest[0].euler_number
  area5test[i] = propstest[0].area

area6test = np.zeros(t6test.shape[0])
perimeter6test = np.zeros(t6test.shape[0])
major_axis_length6test = np.zeros(t6test.shape[0])
euler6test = np.zeros(t6test.shape[0])
for i in range(0,t6test.shape[0]):
  propstest = measure.regionprops(t6test[i,:,:])
  area6test[i] = propstest[0].area
  perimeter6test[i] = propstest[0].perimeter
  major_axis_length6test[i] = propstest[0].major_axis_length
  euler6test[i] = propstest[0].euler_number
X5test = np.zeros((t5test.shape[0],2))
for i in range(0,t5test.shape[0]):
  X5test[i] = [major_axis_length5test[i], area5test[i]]
  
X6test = np.zeros((t6test.shape[0],2))
for i in range(0,t6test.shape[0]):
  X6test[i] = [major_axis_length6test[i], area6test[i]]

  
Xtest = np.append(X5test,X6test,axis = 0)

print(t5test.shape[0])
print(t6test.shape[0])
print('5s class:\n', X5test)
print('6s class:\n', X6test)
print('Two classes together:\n', Xtest)

failstest = 0

for i in X5test:
  if(np.dot(w, i) < T):     
     failstest += 1
    
for i in X6test:
  if(np.dot(w, i) > T):
     failstest += 1

print('Accuracy: ',(1-(failstest/Xtest.shape[0]))*100)