#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A 3D plot script for spherical coordinates.
"""
__author__ = 'Asmita Pramanik'
__email__ = 'asmitap2@illinois.edu'

import numpy as np
from math import pi
import matplotlib.pyplot as plt

def SphericalToCartesian(radius, azimuth, zenith):
    """Converts spherical coordinates to cartesian.
        Here, r -> radius
            a -> azimuth
            b -> zenith
            """
    
    x = radius * np.sin(azimuth) * np.cos(zenith)
    y =  radius * np.sin(azimuth) * np.sin(zenith)
    z = radius * np.cos(azimuth)
    
    return x,y,z


print(SphericalToCartesian(1, 0, 0))

fig = plt.figure() 
axes = fig.gca(projection='3d')  # make 3d axes
r = np.linspace(0, 1)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
x, y, z = SphericalToCartesian(r, theta, phi)
axes.plot(x, y, z)




#the following lines are unit tests for the program
arrayOne = SphericalToCartesian(1, 0, 0)

arrayTwo = SphericalToCartesian(1, pi, pi)

arrayThree = SphericalToCartesian(1 , 2*pi, 2*pi)

arrayFour = SphericalToCartesian( 1, -pi, -2*pi)

arrayFive = SphericalToCartesian(1, -2*pi, -pi)


#np.allclose() function is used to find if two arrays are element-wise equal within a tolerance
assert np.allclose(arrayOne, (0,0,1), rtol=1e-05, atol=1e-08, equal_nan=False), "incorrect"
assert np.allclose(arrayTwo, (0.0547, 0.003003, 0.998497), rtol=1e-05, atol=1e-08, equal_nan=False), "incorrect"
assert np.allclose(arrayThree, (0.10878, 0.011977, 0.99399), rtol=1e-05, atol=1e-08, equal_nan=False), "incorrect"



