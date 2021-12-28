# Enter your code here. Read input from STDIN. Print output to STDOUT
# Question: A large elevator can transport a maximum of 9800 pounds. Suppose a
# load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean
# of u = 205 pounds and a standard deviation of a = 15 pounds. Based on this
# information, what is the probability that all 49 boxes can be safely loaded
# into the freight elevator and transported?

import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

maximum = float(input())
n = int(input())
mean = int(input())
std = int(input())
    
new_std = std * (n ** 0.5)
new_mean = mean * n

print(round(cumulative(new_mean, new_std, maximum), 4))
