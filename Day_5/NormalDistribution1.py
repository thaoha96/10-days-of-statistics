# Enter your code here. Read input from STDIN. Print output to STDOUT
# In a certain plant, the time taken to assemble a car is a random variable, , having a normal distribution with a mean of  hours and a standard deviation of  hours. What is the probability that a car can be assembled at this plant in:

# Less than 19.5 hours?
# Between 20 and 22 hours?
import math 

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean)/(std*(2**0.5))))


initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

print(round(cumulative(mean, std, less_period),3))
print(round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]),3))