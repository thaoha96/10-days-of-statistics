# Enter your code here. Read input from STDIN. Print output to STDOUT
# Question: The number of tickets purchased by each student for the
# University X vs. University Y football game follows a distribution that has
# a mean of u = 2.4 and a standard deviation of 20.
# A few hours before the game starts, 100 eager students line up to purchase
# last-minute tickets. If there are only 250 tickets left, what is the
# probability that all 100 students will be able to purchase tickets?


import math

number_of_tickets = int(input())
n = int(input())
mean = float(input())
std = float(input())

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean)/ (std * (2 ** 0.5) )))

new_mean = mean * n 
new_std = std * (n ** 0.5)
    
print(round(cumulative(new_mean, new_std, number_of_tickets),4))