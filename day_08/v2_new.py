#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:17:45 2023

@author: anup
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


__author__ = "Asmita Pramanik"
__email__ = "asmitap2@illinois.edu"

"""

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":

    dx = 0.25

    # set x with 1 ghost cell on both sides:
    x = np.arange(-dx, 10 + 2 * dx, dx)

    t_lower = 200.0
    
    # t_upper = 1000.0, we commented this out to check how our plots change with changing variables

    nPts = len(x)  #given
    
    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    #d = np.zeros(nPts)
    
    
    # lambda value:
    lam = 10
    
    #defining sun heat
    sun_heat = 100
    
    #initializing Q "heat"
    Q = np.zeros(nPts)
    
    
    Q[(x>3) & (x<7)] = sun_heat
    
    
    dz = x[1] - x[0]  #determining dz
    dz2 = dz * dz   #finding dz^2
    
 # ////////////////////// this portion of code works on time dependence /////////////////////////////
    
    nDays = 3    #number of days
    local_time = 0  #local time
    lon = 100        #longitude (can be changed to analyze plots)
    dt = 1        # time given in hours
    times = np.arange(0, nDays * 24, dt) # also determined in hours
    
    temp= [] #initialising array of times to generate contour plot
    
    
    # we put the following two lines before the for loop to generate a single image instead of several images
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111)
    
    
    for hour in times:
        ut = hour % 24
        local_time = lon/15 + ut
        factor = -np.cos(local_time * 2*np.pi / 24)
        if factor < 0:
            factor = 0
        Q_euv = np.zeros(nPts) #EUV : Extreme Ultra-Violet 
        Q_euv[(x>3)&(x<7)] = sun_heat * factor
        
        d = (Q + Q_euv)*(dz**2)/lam
        
        # boundary conditions (bottom - fixed):
        a[0] = 0
        b[0] = 1
        c[0] = 0
        d[0] = t_lower
        
        # top - fixed:
        a[-1] = 1
        b[-1] = -1
        c[-1] = 0
        d[-1] = 0
        
        # Add a source term:
        
        # solve for Temperature:
        t = solve_tridiagonal(a, b, c, d)
        temp.append(t)
        
        
    temp = np.array(temp).T
    alt = 100 + 40 * x
   

     
    plt.contourf(times,alt,temp,cmap="plasma")
    plt.colorbar(label="Temperature (K)")
    plt.xlabel("Time (hrs)")
    plt.ylabel("Altitude (km)")
    plt.title("Temperature over specified Longitude, " + str(lon))
    
    
    
    
    
    
    
    
    #ax.plot(x,t)
    #ax.set_ylabel("Temperature")
    # ax.set_xlabel("Altitude")
    # ax.set_title("Temperature vs Altitude")
    
    # plotfile = 'conduction_v1b.png'
    # print('writing : ',plotfile)    
    # fig.savefig(plotfile)