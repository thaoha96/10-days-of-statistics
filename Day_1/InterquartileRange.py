#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(size, values):
        if size % 2 == 0:
            median = float((values[int(size/2)-1] + values[int(size/2)]) / 2)
        else:
            median = float(values[int(size/2)])
        return median
    
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for i in range(len(values)):
        arr = arr + ([values[i]]*freqs[i])
    
    arr.sort()
    median_arr = median(len(arr),arr)    
        
    # Verify that the total data is even or odd
    size = len(arr)

    if size % 2 == 0:
        data_low = arr[0:int(size/2)]
        data_high = arr[int(size/2):size]
    else:
        data_low = arr[0:int(size/2)]
        data_high = arr[int(size/2)+1:size]

    # Get the final result and print on the screen
    low = median(len(data_low), data_low)
    high = median(len(data_high), data_high)
    print(round(high - low,1))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
