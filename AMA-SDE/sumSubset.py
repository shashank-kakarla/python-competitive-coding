def subsetSums(arr, l, r,result, sum=0):
 
    if l > r:
        result.append(sum)
        return
    subsetSums(arr, l + 1, r, result, sum + arr[l])
    
    subsetSums(arr, l + 1, r, result, sum)
 
 
arr = [3,5,-2]
n = len(arr)
result = []
subsetSums(arr, 0, n - 1, result)
result.sort(reverse=True)
print(result[:3])
