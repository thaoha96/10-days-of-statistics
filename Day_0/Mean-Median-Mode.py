import numpy as np

num_of_elements = int(input())
elements = list(map(int,input().split()))

import numpy as np
print(np.mean(elements))
print(np.median(elements))
def get_mode(xs):
    values, counts = np.unique(xs, return_counts=True)
    max_count_index = np.argmax(counts) #return the index with max value counts
    return values[max_count_index]
print(get_mode(elements))