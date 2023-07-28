#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:43:27 2023

@author: Asmita Pramanik
"""


import datetime as dt
import matplotlib.pyplot as plt


def read_ascii_file(filename,index):
    
    """ This function takes in filename and index and reads an ASCII file """
    
    data = {"time":[],
           "symh":[]}
    
    nLines = 3
    with open("/Users/anup/Desktop/personalprojects/swsss2023/day_02/omniweb.gsfc.nasa.gov_staging_omni_min_def_GDDvkRYnIl_ascii.lst.txt") as f:
        
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
            times_list.append(datetime1)
            
            
            data["time"].append(datetime1)
            data['symh'].append(int(temp[index]))
        
    return data


    #//////////////////FUNCTION CALL//////////////////////////

filename = "/Users/anup/Desktop/personalprojects/swsss2023/day_02/omniweb.gsfc.nasa.gov_staging_omni_min_def_GDDvkRYnIl_ascii.lst.txt"
index = -1
#year, day, hour, minute, data = read_ascii_file(filename,index)

data_test = read_ascii_file(filename,index)

time = data_test["time"]
data1 = data_test["symh"]

fig,ax = plt.subplots()

ax.plot(time,data1,marker='.',c='r',
        label='This is a plot',alpha=0.8)
#ax.set_xlim([dt.datetime(2013, 3, 16, 0, 6),dt.datetime(2013, 3, 16, 0, 2)])

ax.set_xlabel('Time')
ax.set_ylabel('SYMH (nT)')
ax.grid(True)
ax.legend()
plt.xticks(rotation=40)
plt.show()
    
        

    