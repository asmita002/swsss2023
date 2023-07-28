#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:30:55 2023

@author: Asmita Pramanik
"""


import datetime as dt
import matplotlib.pyplot as plt


def read_ascii_file(filename,index):
    
    """ This function takes in filename, index as arguments and reads an ASCII file """
    
    data = {"time":[],"symh":[]}
        
    nLines = 4
    with open(filename) as f:
        
        for i in range(nLines):
            print(f.readline())  
        
        #------------storing variables to lists-----------------
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
            symh.append(float(temp[index]))

            datetime1 = dt.datetime(int(temp[0]),1,1,int(temp[2]),int(temp[3])) + dt.timedelta(days = int(temp[1])-1)
            #print(datetime1)
            times_list.append(datetime1)
            #print(times_list)
            
            data["time"].append(datetime1)
            data["symh"].append(float(temp[index]))
            
           # my_data = {"time": times_list,
                    #"symh": symh}
        
        return data


    #//////////////////FUNCTION CALL//////////////////////////

filename = "/Users/anup/Desktop/personalprojects/swsss2023/day_02/omni_test.lst"
index = -1

data_test = read_ascii_file(filename,index)

print(data_test)
    
        
