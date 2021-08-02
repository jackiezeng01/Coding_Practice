'''
Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order. 


'''

def insert(num, arr):
    for i in range(1, len(arr)):
        if num >= arr[i-1] and num <= arr[i]:
            temp1 = arr[i]
            # insert elem
            arr[i] = num
            for j in range(i+1, len(arr)):
                temp2 = arr[j]
                arr[j] = temp1
                temp1 = temp2
            return arr
        elif i == len(arr)-1:
            arr[i] = num
            return arr

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,0]
    print(arr)
    num = 20

    arr = insert(num, arr)
    print(arr)
