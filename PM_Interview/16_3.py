'''
Given two lists(A and B) of unique strings, write a program to determine
 if A is a subset of B. That is, check if all elements from A are 
 containted in B
'''

def is_subset(A, B):
    B_set = set(B)
    for elem in A:
        if elem not in B_set:
            return False
    return True

if __name__ == "__main__":
    A = [1,2,3,4,5,7]
    B = [1,2,3,4,5,6,7]
    res = is_subset(A, B)
    print(res)
