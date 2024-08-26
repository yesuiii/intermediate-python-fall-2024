#Imports numpy package as np
import numpy as np

def max(data):
    #Takes the data as np.array and returns the maximum value
    return np.array(data).max()

def min(data):
    #Takes the data as np.array and returns the minimum value
    return np.array(data).min()

def median(data):
    #Takes the data returns the median value
    return np.median(data)