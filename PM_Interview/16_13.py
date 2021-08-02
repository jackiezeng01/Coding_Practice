'''
Given two sorted arrays, write a function to merge them in sorted order into a new array
'''

def merge_sorted(l1, l2):
    res = []
    p1, p2 = 0, 0

    while p1<len(l1) or p2<len(l2):
        if  p1<len(l1) and p2<len(l2):
            if l1[p1] < l2[p2]:
                res.append(l1[p1])
                p1 += 1
            else:
                res.append(l2[p2])
                p2 += 1
        elif p1<len(l1):
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1
    return res

if __name__ == "__main__":
    l1 = [1,2,7]
    l2 = [3,4,8]
    res = merge_sorted(l1, l2)
    print(res)