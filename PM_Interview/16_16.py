'''
You are given an integer array which was sorted, but then rotated. It contains
 all distinct elements. Find the minimum value. For example, the array might be
 [6,8,9,11,15,20,3,4,5]. The minimum value would obviously be 3
'''

def find_min_in_rotated(arr):
    # check first elem:
    if arr[0] < arr[-1]:
        return arr[0]
    # find the point where arr[i] > arr[i+1]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return arr[i+1]

if __name__ == "__main__":
    arr = [6,8,9,11,15,20,3,4,5]
    res = find_min_in_rotated(arr)
    print(res)