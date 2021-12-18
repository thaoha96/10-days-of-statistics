def weightedMean(X, W):
    # Write your code here
    sums = 0
    for i in range(len(X)):
        sums = sums + (X[i]*W[i])
    print(round(sums/sum(W),1))
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)