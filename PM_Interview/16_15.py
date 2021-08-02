'''
Implement binary search. That is, given a sorted array of integers and a value, find the location of that value
'''

def binary_search(arr, n):
    return helper(arr, n, 0, len(arr)-1)
    

def helper(arr, n, low, high):
    if high < low:
        return False
    mid = (high+low)//2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n: #elem must be in lower half
        return helper(arr, n, low, mid-1)
    else: # elem must be in higher half
        return helper(arr, n, mid+1, high)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    res = binary_search(arr,3)
    print(res)