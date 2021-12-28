# Enter your code here. Read input from STDIN. Print output to STDOUT
#Task
#A random variable, X, follows Poisson distribution with mean of .
#Find the probability with which the random variable X is equal to 5.



def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n>1:
        return factorial(n-1)*n
        
# Set data
mean = float(input())
k = float(input())
e = 2.71828
        
def Poisson(mean,k):
    result = ((mean**k)*(e**(-mean)))/(factorial(k))
    return result

print(Poisson(mean,k))