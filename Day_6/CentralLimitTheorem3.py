# Enter your code here. Read input from STDIN. Print output to STDOUT
# Confidence interval

# Question: You have a sample of 100 values from a population with mean u = 500
# and with standard deviation a = 80. Compute the interval that covers the
# middle 95% of the distribution of the sample mean; in other words, compute
# A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note
# that z is the z-score

import math

n = int(input())
mean = int(input())
std = int(input())
probability = float(input())
z_score = float(input())

new_std = std / (math.sqrt(n))
ci = z_score * new_std

print(round(mean - ci, 2))
print(round(mean + ci, 2))
