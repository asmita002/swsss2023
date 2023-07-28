#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:35:16 2023

@author: anup
"""

from wam_ipe_plotter import plot_tec, save_tec


import sys

infilename = sys.argv[1:]

for i in infilename:
    save_tec(i)


# save_tec(infilename)