'''
Implement insertion sort

this one kinda was difficult
'''

def insertion_sort(arr):
    curr = 0
    for i in range(1, len(arr)):
        elem = arr[i]
        
        j = i-1
        while j>=0 and elem < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem 
    return arr

if __name__ == "__main__":
    arr = [15,2,34,78,3,2,1]
    res = insertion_sort(arr)
    print(res)