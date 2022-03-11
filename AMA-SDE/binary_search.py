def binary_search(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[len(arr)-1] < target:
        return -1
    
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid+1   
    return -1

def get_first(arr, target):
    if arr[0] ==  target:
        return 0
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
def get_last(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

arr = [1, 2, 2, 2, 2, 2, 3, 6, 8, 10]
print(binary_search(arr, 2))
print(get_first(arr, 2))
print(get_last(arr, 2))