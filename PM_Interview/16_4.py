'''
You are given a two-dimensional array of sales data where the first column
 is a product ID and the second column is the quantity. Write a function 
 to take this list of data and return a new two-dimensional arraty with the
 total sales for each product ID
'''

def congregate_sales(arr):
    # key: product id, val: total sales
    d = dict()
    for i, elem in enumerate(arr[0]):
        if elem in d:
            d[elem] += arr[1][i]
        else:
            d[elem] = arr[1][i]
    
    #turn dict to array
    return [list(d.keys()), list(d.values())]

if __name__ == "__main__":
    arr = [[211,262,211,216], [4,3,5,6]]
    print(congregate_sales(arr))

