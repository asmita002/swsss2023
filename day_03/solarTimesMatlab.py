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

tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T # convert from g/cm3 to kg/m3
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]

# We will be using the same time index as before.
time_array_tiegcm = time_array_JB2008

# This is a HDF5 dataset object, some similarity with a dictionary
print('Key within dataset:',list(loaded_data.keys()))

tiegcm_dens_reshaped = np.reshape(tiegcm_dens, (nofLst_tiegcm,nofLat_tiegcm, nofAlt_tiegcm, 8760), order='F')
print(JB2008_dens_reshaped.shape, tiegcm_dens_reshaped.shape)

#%%
"""
TODO: Plot the atmospheric density for 310 KM for all time indexes in
      time_array_tiegcm
"""




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

from scipy import interpolate

x = np.arange(0,10) #x coordinate
y = np.exp(-x/3.0)

# this generates 1D interpolant function
interp_func_1D = interpolate.interp1d(x,y)

# Let's select some new points
xnew = np.arange(0, 9, 0.1) #generates a range of values between 0 and 9

# use interpolation function returned by `interp1d`
ynew = interp_func_1D(xnew)

interp_func_1D_cubic = interpolate.interp1d(x,y,kind='cubic') #cubic polynomial fit

ycubic = interp_func_1D_cubic((xnew))

interp_func_1D_quadratic = interpolate.interp1d(x,y,kind="quadratic")
yquadratic = interp_func_1D_quadratic(xnew) 

# drawing interpolated data graph

plt.subplots(1, figsize=(10, 6))
plt.plot(x, y, 'o', xnew, ynew, '*',xnew, ycubic, '--',xnew, yquadratic, '--',linewidth = 2)
plt.legend(['Inital Points','Interpolated line-linear','Interpolated line-cubic','Interpolated line-quadratic'], fontsize = 16)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
plt.title('1D interpolation', fontsize=18)
plt.grid()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
#%%
"""
Data Interpolation (3D)

Now, let's us look at how to do data interpolation with scipy
"""

from scipy.interpolate import RegularGridInterpolator

# creating set of sample data that we will be using 3D interpolant on

def function_1(x,y,z):
    return 2*x**3 + 3*y**2 - z

x = np.linspace(1,4,11)
y = np.linspace(4,7,22)
z = np.linspace(7,9,33)
xg , yg , zg = np.meshgrid(x, y, z, indexing = 'ij', sparse = True)

sample_data = function_1(xg,yg,zg)

#generating interpolating function

interpolated_function_1 = RegularGridInterpolator((x,y,z), sample_data)
                                                  
# example set of points [[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]]      
pts = np.array([[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]]) 
print("This output is generated using interpolation method:", interpolated_function_1(pts))   
print("This output is from true function:", function_1(pts[:,0], pts[:,1], pts[:,2]))                 
                                                  
#%%
"""
Saving mat file

Now, let's us look at how to we can save our data into a mat file
"""

from scipy.io import savemat

a = np.arange(20)
mdic = {"a": a, "label": "experiment","v": 1} # Using dictionary to store multiple variables
savemat("matlab_matrix.mat", mdic)

#%%
"""
Assignment 2 (a)

The two data that we have been working on today have different discretization 
grid.

Use 3D interpolation to evaluate the TIE-GCM density field at 400 KM  altitude on 
February 1st, 2002, with the discretized grid used for the JB2008 
((nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008).
"""
from scipy.interpolate import RegularGridInterpolator

#printing the altitude values in two different sets of data
print("This is list of TIE-GCM altitudes: \n\n" , altitudes_tiegcm) 
print("\n\n\n")
print("This is list of JB2008 altitudes: \n\n" , altitudes_JB2008)

print("\n\n\n")

#printing lJB2008 data required
print("This is list of JB2008 lst: \n\n" , localSolarTimes_JB2008) 
print("\n\n\n")
print("This is list of JB2008 lat: \n\n" , latitudes_JB2008)

print("\n\n\n")

#printing tie-gcm data required
print("This is list of tie-gcm lst: \n\n" , localSolarTimes_tiegcm) 
print("\n\n\n")
print("This is list of tie-gcm lat: \n\n" , latitudes_tiegcm)

# first find the time index
time_index = 31 * 24

# generating interpolating function
generateInterpolantFunction = RegularGridInterpolator((localSolarTimes_tiegcm, latitudes_tiegcm, altitudes_tiegcm),
tiegcm_dens_reshaped[:,:,:, time_index], bounds_error = False, fill_value = None)

# for an alternative method, you can use mesh grid
density_400_alt_tiegcm = np.zeros((24,20))
for i in range(len(localSolarTimes_JB2008)):
    for j in range(len(latitudes_JB2008)):
        density_400_alt_tiegcm[i,j] =  generateInterpolantFunction((localSolarTimes_JB2008[i], latitudes_JB2008[j], 400))
        
# this is our density_400_alt_tiegcm grid
print("This is our density_400_alt_tiegcm grid\n", density_400_alt_tiegcm)

#time to plot the grid                                                                                                                                  
fig, axs = plt.subplots(2, figsize=(15, 10), sharex=True)

cs = axs[0].contourf(localSolarTimes_JB2008, latitudes_JB2008, density_400_alt_tiegcm.T)
axs[0].set_title('TIE-GCM density at Altitude = 400 km, t = {} hrs'.format(time_index), fontsize=18)
axs[0].set_ylabel("Latitudes", fontsize=18)
axs[0].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig.colorbar(cs,ax=axs[0])
cbar.ax.set_ylabel('Density')

alt = 400
hi = np.where(altitudes_JB2008==alt)

cs = axs[1].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_index].squeeze().T)
axs[1].set_title('JB2008 density at Altitude = 400 km, t = {} hrs'.format(time_index), fontsize=18)
axs[1].set_ylabel("Latitudes", fontsize=18)
axs[1].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig.colorbar(cs,ax=axs[1])
cbar.ax.set_ylabel('Density')

axs[1].set_xlabel("Local Solar Time", fontsize=18)



#%%
"""
Assignment 2 (b)

Now, let's find the difference between both density models and plot out this 
difference in a contour plot.
"""

JB2008_density_400km_resized = JB2008_dens_reshaped[:,:,hi,time_index].squeeze()

diffInDensity = density_400_alt_tiegcm - JB2008_density_400km_resized
print(diffInDensity)

fig, axs = plt.subplots(1, figsize=(18,12), sharex=True)

cs = axs.contourf(localSolarTimes_JB2008, latitudes_JB2008, diffInDensity.T)

axs.set_title('Density Difference', fontsize=18)
axs.set_ylabel("Latitudes", fontsize=18)
axs.tick_params(axis = 'both', which = 'major', labelsize = 16)


#%%
"""
Assignment 2 (c)

In the scientific field, it is sometime more useful to plot the differences in 
terms of absolute percentage difference/error (APE). Let's plot the APE 
for this scenario.

APE = abs(tiegcm_dens-JB2008_dens)/tiegcm_dens
"""