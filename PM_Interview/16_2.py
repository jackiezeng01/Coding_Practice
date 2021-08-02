'''
Reverse the order of elements in an array (without creating a new array)
'''

def reverse_array(arr):
    p1 = 0
    p2 = len(arr)-1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1+=1
        p2-=1
    return arr

if __name__ == "__main__":
    arr = [1,2,3,4]
    print(arr)
    print("reversed: ", reverse_array(arr))

