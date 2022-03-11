def two_sum(arr, value):
    sum = {}
    for val in arr:
        if value - val not in sum.keys():
            sum[val] = 0
        else:
            return True
    return False

A = [1, 2, 4, 5, 6]
print(two_sum(A, 13))