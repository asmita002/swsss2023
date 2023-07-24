#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:51:42 2023

@author: Asmita Pramanik
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1) #default num is 50
plt.plot(x , np.exp( x ))
plt.xlabel(r'$0 <= x < 1$')  #\leq basically mean less than or equal to
plt.ylabel(r'$e^x$')
plt.title('Exponential function')
plt.show() #shows plot, can be saved