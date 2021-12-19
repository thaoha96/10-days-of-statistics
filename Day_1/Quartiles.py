#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(size, values):
        if size % 2 == 0:
            median = (values[int(size/2)-1] + values[int(size/2)]) / 2
        else:
            median = values[int(size/2)]
        return int(median)

def quartiles(arr):
    # Write your code here
    # Define functions
    size = len(arr)
    res = []
    
    # Verify that the total data is even or odd
    if size % 2 == 0:
        data_low = arr[0:int(size/2)]
        data_high = arr[int(size/2):size]
    else:
        data_low = arr[0:int(size/2)]
        data_high = arr[int(size/2)+1:size]
        
    print(data_low)
    # Get the final result and print on the screen
    res.append(median(len(data_low), data_low))
    res.append(median(size, arr))
    res.append(median(len(data_high), data_high))
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))
    
    # Array need to be in order to get median
    data.sort()
    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()