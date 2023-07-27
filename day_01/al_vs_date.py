#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:24:23 2023

@author: anup
"""

#importing datetime function from datetime package
from datetime import datetime
#importing get_omni_data from swmfpy.web package
from swmfpy.web import get_omni_data
import matplotlib.pyplot as plt


# the following variables denote the time frame within which we are 
# evaluating the auroral electrojets
start_time = datetime(2002, 10, 31)
end_time = datetime(2002, 11, 1)


# returns a dictionary 
data = get_omni_data(start_time, end_time)


#plot with al as y-axis and dates as x-axis
plt.plot(data['times'], data['al'] )


