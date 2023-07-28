#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome to Space Weather Simulation Summer School Day 3

Today, we will be working with various file types, doing some simple data 
manipulation and data visualization

We will be using a lot of things that have been covered over the last two days 
with minor vairation.

Goal: Getting comfortable with reading and writing data, doing simple data 
manipulation, and visualizing data.

Task: Fill in the cells with the correct codes

@author: Peng Mun Siew
"""

#%% 
"""
This is a code cell that we can use to partition our data. (Similar to Matlab cell)
We hace the options to run the codes cell by cell by using the "Run current cell" button on the top.
"""
print ("Hello World")

#%%
"""
Creating a random numpy array
"""
# Importing the required packages
import numpy as np

# Generate a random array of dimension 10 by 5
data_arr = np.random.randn(10,5)
print(data_arr)

#%%
"""
TODO: Writing and reading numpy file
"""
# Save the data_arr variable into a .npy file
np.save('test_np_save.npy',data_arr)

# Load data from a .npy file
data_arr_loaded = np.load('test_np_save.npy')

# Verification that the loaded data matches the initial data exactly
print(np.equal(data_arr,data_arr_loaded))
print(data_arr == data_arr_loaded)


#%%
"""
TODO: Writing and reading numpy zip archive/file
"""
# Generate a second random array of dimension 8 by 1
data_arr2 = np.random.randn(8,1)
print(data_arr2)

# Save the data_arr and data_arr2 variables into a .npz file
np.savez('test_savez.npz', data_arr, data_arr2)

# Load the numpy zip file
npzfile = np.load("test_savez.npz")
# Verify that the loaded data matches the initial data
print(npzfile)
print('Variable names within this file:', sorted(npzfile.files))
#%%
"""
Error and exception
"""
# Exception handling, can be use with assertion as well
try:
    # Python will try to execute any code here, and if there is an exception 
    # skip to below 
    print(np.equal(data_arr,npzfile).all())
except:
    # Execute this code when there is an exception (unable to run code in try)
    print("The codes in try returned an error.")
    print(np.equal(data_arr,npzfile['arr_0']).all())
    
#%%
"""
TODO: Error solving 1
"""
# What is wrong with the following line? 
np.equal(data_arr,data_arr2)
# ----Ans----The arrays of different size

#%%
"""
TODO: Error solving 2
"""
# What is wrong with the following line? 
np.equal(data_arr2,npzfile['data_arr2'])
#-----we are giving the wrong key

#%%
"""
TODO: Error solving 3
"""
# What is wrong with the following line? 
np.equal(data_arr2,npzfile['arr_1'])
#-----use np instead of numpy as we have already mentioned "import numpy as np" on the top


#%%
"""
Loading data from Matlab
"""

# Import required packages
import numpy as np
from scipy.io import loadmat

dir_density_Jb2008 = '/Users/anup/Desktop/personalprojects/swsss2023/day_03/2002_JB2008_density.mat'

# Load Density Data
try:
    loaded_data = loadmat(dir_density_Jb2008)
    print (loaded_data)
except:
    print("File not found. Please check your directory")


# Uses key to extract our data of interest
JB2008_dens = loaded_data['densityData']

# The shape command now works
print(JB2008_dens.shape)

#%%
"""
Data visualization I

Let's visualize the density field for 400 KM at different time.
"""
# Import required packages
import matplotlib.pyplot as plt

# Before we can visualize our density data, we first need to generate the 
# discretization grid of the density data in 3D space. We will be using 
# np.linspace to create evenly sapce data between the limits.

localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
nofAlt_JB2008 = altitudes_JB2008.shape[0]
nofLst_JB2008 = localSolarTimes_JB2008.shape[0]
nofLat_JB2008 = latitudes_JB2008.shape[0]

# We can also impose additional constraints such as forcing the values to be integers.
time_array_JB2008 = np.linspace(0,8759,5, dtype = int)

# For the dataset that we will be working with today, you will need to reshape 
# them to be lst x lat x altitude
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008,nofLat_JB2008,
                                               nofAlt_JB2008,8760), order='F') # Fortran-like index order

#%%
"""
TODO: Plot the atmospheric density for 300 KM for the first time index in
      time_array_JB2008 (time_array_JB2008[0]).
"""

import matplotlib.pyplot as plt
%matplotlib inline 
# altitude is 300 km
alt = 300
hi = np.where(altitudes_JB2008==alt)

# Create a canvas to plot our data on. Here we are using a subplot with 5 spaces for the plots.
fig, axs = plt.subplots((5), figsize=(15, 10*2), sharex=True)

length = len(time_array_JB2008)

for ik in range (length):
    cs = axs[ik].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
    axs[ik].set_title('JB2008 density at 300 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    # Make a colorbar for the ContourSet returned by the contourf call.
    cbar = fig.colorbar(cs,ax = axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18)





#%%
"""
TODO: Plot the atmospheric density for 400 KM for all time indexes in
      time_array_JB2008
"""
import matplotlib.pyplot as plt
%matplotlib inline  #allows the plots to be displayed directly within the notebook

# set altitude as 400 km 
alt = 400         

# finds the index (or indices) where the elements in the array altitudes_JB2008 are 
# equal to the value stored in alt (which is 400). This will be used later to extract data 
# corresponding to this specific altitude.
hi = np.where(altitudes_JB2008 == alt)

# Create a canvas to plot our data on. Here we are using a subplot for the plots.
# This line creates a figure and a set of subplots within that figure. 
# It creates one subplot (1) and sets the size of the figure to be (15, 4) inches. 
# sharex=True means that the x-axis will be shared among the subplots (if there were more than one).
fig, axs = plt.subplots(1, figsize=(15, 4), sharex=True)

ik = 0
cs = axs.contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
axs.set_title('JB2008 density at 400 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
axs.set_ylabel("Latitudes", fontsize=18)
axs.tick_params(axis = 'both', which = 'major', labelsize = 16)
    
# Make a colorbar for the ContourSet returned by the contour call.
cbar = fig.colorbar(cs,ax=axs)
cbar.ax.set_ylabel('Density')

axs.set_xlabel("Local Solar Time", fontsize=18)    


#%%
"""
Assignment 1

Can you plot the mean density for each altitude at February 1st, 2002?
"""

import matplotlib.pyplot as plt
# this is the time index corresponding to the given date
listofMean = []
time_index = 31 * 24
JB2008_dens_feb1 = JB2008_dens_reshaped[:,:,:,time_index]
print('The dimension of the data are as follows (local solar time,latitude,altitude):', JB2008_dens_feb1.shape)

for k in range(len(altitudes_JB2008)):
    calculatedMean = np.mean(JB2008_dens_feb1[:,:,k])
    listofMean.append(calculatedMean)

print(listofMean)

plt.subplots(1, figsize=(10, 6))
plt.semilogy(altitudes_JB2008 , listofMean,linewidth = 2)
plt.xlabel('Altitude', fontsize=20)
plt.ylabel('Density', fontsize=20)
plt.title('dens vs alt', fontsize=18)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)




#%%
"""
Data Visualization II

Now, let's us work with density data from TIE-GCM instead, and plot the density 
field at 310km

"""
# Import required packages
import h5py
loaded_data = h5py.File('/Users/anup/Desktop/personalprojects/swsss2023/day_03/2002_TIEGCM_density.mat')

# This is a HDF5 dataset object, some similarity with a dictionary
print('Key within dataset:',list(loaded_data.keys()))

tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T # convert from g/cm3 to kg/m3
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]

# We will be using the same time index as before.
time_array_tiegcm = time_array_JB2008


#%%
"""
TODO: Plot the atmospheric density for 310 KM for all time indexes in
      time_array_tiegcm
"""

import matplotlib.pyplot as plt

for k in range(len(altitudes_JB2008)):
    calculatedMean = np.mean(JB2008_dens_feb1[:,:,k])
    listofMean.append(calculatedMean)
    
time_array_tiegcm


#%%
"""
Assignment 1.5

Can you plot the mean density for each altitude at February 1st, 2002 for both 
models (JB2008 and TIE-GCM) on the same plot?
"""



#%%
"""
Data Interpolation (1D)

Now, let's us look at how to do data interpolation with scipy
"""


#%%
"""
Data Interpolation (3D)

Now, let's us look at how to do data interpolation with scipy
"""



#%%
"""
Saving mat file

Now, let's us look at how to we can save our data into a mat file
"""

#%%
"""
Assignment 2 (a)

The two data that we have been working on today have different discretization 
grid.

Use 3D interpolation to evaluate the TIE-GCM density field at 400 KM on 
February 1st, 2002, with the discretized grid used for the JB2008 
((nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008).
"""





#%%
"""
Assignment 2 (b)

Now, let's find the difference between both density models and plot out this 
difference in a contour plot.
"""





#%%
"""
Assignment 2 (c)

In the scientific field, it is sometime more useful to plot the differences in 
terms of absolute percentage difference/error (APE). Let's plot the APE 
for this scenario.

APE = abs(tiegcm_dens-JB2008_dens)/tiegcm_dens
"""