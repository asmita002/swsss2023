#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:44:28 2023

@author: Asmita Pramanik
"""

import netCDF4 as nc
import matplotlib.pyplot as plt 
import numpy as np

dataset = nc.Dataset('/Users/anup/Desktop/wfs.t18z.20230726_15 2/wfs.t18z.ipe05.20230726_151500.nc')



def plot_tec(dataset, figsize = (12,6)):
    
    """The following function generates a colormesh plot of TEC"""
    
    fig, ax = plt.subplots(nrows = 1,ncols = 1,figsize = figsize)
    
    x = dataset["lon"][:] #setting x axis
    y = dataset["lat"][:] #setting y axis
    z = dataset["tec"][:] #finding tec
    
    ax.pcolormesh(x, y, z, shading = "auto")
    
    ax.set_title("Total Electron Content", fontsize = "20")
    ax.set_xlabel("Longitude" , fontsize = "18")
    ax.set_ylabel("Latitude", fontsize = "18")
    
    return fig, ax
    
    
# --------------------------------------------------------------------------------------------------------------------#



def savePlotAsPNG(infilename):             #takes in infilename as arg

""" This function saves a returned image from another function as a png"""

    datasetnew = nc.Dataset(infilename)    #reads the datafile and returns the dataset and stores it in datasetnew
    fig, ax = plot_tec(datasetnew, figsize = (12,6))  
    outfilename = infilename + '.png'   #adds the .png extension to the filename
    
    fig.savefig(outfilename) #saves figure as outfilename 

infilename = "/Users/anup/Desktop/wfs.t18z.20230726_15 2/wfs.t18z.ipe05.20230726_151500.nc"

# function declaration
savePlotAsPNG(infilename)     








        

#def wap_ipe(dataset, figsize = (12,6)):
    #fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = figsize)
    #x = dataset["alt"][:] #setting x axis
    #y = dataset["lat"][:] #setting y axis
    #z = dataset["HmF2"][:] #finding tec
    
    #ax.pcolormesh(x, y, z, cmap = "magma")
    #ax.set_title("Total Electron Content", fontsize = "20")
    #ax.set_xlabel("Longitude" , fontsize = "18")
    #ax.set_ylabel("Latitude", fontsize = "18")
    
    
    
    #return fig, ax
 #wap_ipe(dataset, figsize = (12,6))   
