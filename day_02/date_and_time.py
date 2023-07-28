#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:18:47 2023

@author: Asmita Pramanik
"""

import datetime as dt
import matplotlib.pyplot as plt





nLines = 3
with open("/Users/anup/Desktop/personalprojects/swsss2023/day_02/omni_test.lst") as f:
    
        
    for i in range(nLines):
        print(f.readline())
    
    
    header = f.readline() 
    vars = header.split()
    
    year = []
    day = []
    hour = []
    minute = []
    symh = []
    times_list = []

   
    for line in f:
        temp = line.split()
        
        year.append(int(temp[0]))
        day.append(int(temp[1]))
        hour.append(int(temp[2]))
        minute.append(int(temp[3]))
        symh.append(float(temp[4]))

        datetime1 = dt.datetime(int(temp[0]),1,1,int(temp[2]),int(temp[3])) + dt.timedelta(days = int(temp[1])-1)
        print(datetime1)
        times_list.append(datetime1)
        print(times_list)
       
        # times.append(datetime)
        #sys.exit('check')
        

    






