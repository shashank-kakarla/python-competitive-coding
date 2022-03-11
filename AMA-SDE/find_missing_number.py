def getSum(n):
    return int((n*(n+1))/2)

def findMissingNumber(arr, n):
    sum = 0
    for ar in arr:
        sum = sum + ar
    return getSum(n) - sum

A = [1, 2, 4, 5, 6]
print(type(A))
print(findMissingNumber(A, 6))
