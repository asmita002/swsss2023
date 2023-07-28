#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:18:19 2023

@author: Asmita Pramanik
"""

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np



def read_ascii_file(filename,index, starttime, endtime):
    
    """ This function takes in filename, index as arguments and reads an ASCII file """
    
    data = {"time":[],"symh":[]}
    
        
    nLines = 4
    with open(filename) as f:
        
        for i in range(nLines):
            print(f.readline())  
        
        #-----------------storing variables to lists--------------------
        
        year = []
        day = []
        hour = []
        minute = []
        symh = []
        times_list = []

   
        for line in f:
            temp = line.split() 
        
            year.append(int(temp[0])) # adding year values to empty list 'year'
            day.append(int(temp[1])) # adding day values to empty list 'day'
            hour.append(int(temp[2])) # adding hour values to empty list 'hour'
            minute.append(int(temp[3])) # adding minute values to empty list minute
            symh.append(float(temp[index])) # adding symh values to empty list 'symh'

            datetime1 = dt.datetime(int(temp[0]),1,1,int(temp[2]),int(temp[3])) + dt.timedelta(days = int(temp[1])-1)
            #print(datetime1)
            times_list.append(datetime1)
            #print(times_list)
            
            data["time"].append(datetime1)
            data["symh"].append(float(temp[index]))
            
        #-----------chosing specific time range-------------
        
        time = np.array(data['time'])
        
        #lp is an array of True/False values depending upon the following condition
        lp = (time > starttime)&(time < endtime) 
        
        #printing lp values
        print(lp)
        
        #returning value of ket 'symh' in dictionary 'data'
        symh = np.array(data['symh'])
        
        symh_sel = symh[lp]
        
        print('symh_sel',symh_sel)
        
        data['symh'] = symh_sel
        
        
        return data


    #//////////////////FUNCTION CALL//////////////////////////

filename = "/Users/anup/Desktop/personalprojects/swsss2023/day_02/omni_test.lst"
index = -1


data_test = read_ascii_file(filename,index,dt.datetime(2013, 3, 16, 0, 3) , dt.datetime(2013, 3, 16, 0, 8))

#print(data_test)
    