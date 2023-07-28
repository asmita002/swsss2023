#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:44:09 2023

@author: Asmita Pramanik
"""

#importing necessary packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import datetime as dt

"""The following function opens a file with the specified full path address and 
reads the first three lines. Then it reads the first line of the file and 
stores it in the variable header. The split() function splits the first line based on the number of 
spaces between the words and puts them in a list"""

numberOfLines = 3
with open("/Users/anup/Desktop/personalprojects/swsss2023/day_02/omni_test.lst") as f:
    for i in range(numberOfLines):
        print(f.readline())
        
    header = f.readline()
    vars = header.split()
    print(vars)

    for line in f:
        temp = line.split()
    
 
#//////////////////////////////////////////////////////////////////////////////////////////////////////

