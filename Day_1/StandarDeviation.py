#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean_arr = sum(arr)/len(arr)
    square_diff_sum = 0
    
    for i in range(len(arr)):
        square_diff_sum =  square_diff_sum + (arr[i] - mean_arr)**2
    print(round(math.sqrt(square_diff_sum/len(arr)),1))
        
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
