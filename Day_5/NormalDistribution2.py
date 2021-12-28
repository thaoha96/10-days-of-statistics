# Enter your code here. Read input from STDIN. Print output to STDOUT
# Question: The final grades for a Physics exam taken by a large group of
# students have a mean of mi = 70 and a standard deviation of sigma = 10.
# If we can approximate the distribution of these grades by a normal
# distribution, what percentage of the students:
# 1. Scored higher than 80 (i.e., have a grade > 80)?
# 2. Passed the test (i.e., have a grade >= 60)?
# 3. Failed the test (i.e., have a grade < 60)?
import math

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean)/(std * (2**0.5))))

initial_values = list(map(float,input().split()))
mean = initial_values[0]
std = initial_values[1]
val_first_ques = float(input())
val_third_ques = float(input())

print (round(100 - (cumulative(mean, std, val_first_ques) * 100), 2))
print (round(100 - (cumulative(mean, std, val_third_ques) * 100), 2))
print (round(cumulative(mean, std, val_third_ques) * 100, 2))