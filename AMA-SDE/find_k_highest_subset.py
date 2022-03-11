def sum_subset(arr, left, right, result, resultArr, sum=0):
    
    if left > right:
        result.add(sum)
        return
    
    sum_subset(arr, left +1,right,result,resultArr.append(arr[left]),arr[left]+sum)
    
    sum_subset(arr, left+1, right, result,resultArr, sum)
    

arr = [3,5,-2]
n = len(arr)
k=4
result = resultArr = []
sum_subset(arr, 0, n-1, result, resultArr)
print(result, resultArr)