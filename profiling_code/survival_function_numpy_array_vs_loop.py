#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:36:32 2021

Compares the peformance of scipy survival function acting on a single numpy array 
against calling scipy survival function for every element in the array via a loop

@author: seanbray
"""

import numpy as np
import time
import scipy.stats as spstat
import matplotlib.pyplot as plt
import pandas as pd


#profiling numpy function
numpy_profile = {}
loop_profile = {}
data_lenght = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
for i in data_lenght:
    input_array = np.random.uniform(0,1,i)
    
    start = time.process_time()
    spstat.norm.logsf(input_array)
    numpy_profile[i] = time.process_time() - start

#profiling for loop
for i in data_lenght:
    input_array = np.random.uniform(0,1,i)
    
    start = time.process_time()
    for j in input_array:
        spstat.norm.logsf(j)
    loop_profile[i] = time.process_time() - start



#plotting results
fig = plt.figure(figsize=(15,6))
plt.plot(pd.Series(numpy_profile), label="numpy_array")
plt.plot(pd.Series(loop_profile), label="for_loop")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of data points")
plt.ylabel("Run time in seconds")
plt.title("Calling scipy survival function \n with single numpy array v.s. via for loop")
plt.legend()
plt.show()

