"""Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degree. Can you do this in place?"""

import math

def rotateMatrix(mat):
    n = len(mat)
    layers = math.ceil(n/2)
    for i in range(layers):
        end = n-i-1
        if i == end:
            break
        else:
            for j in range(i, end):
                offset = j-i

                # print("top:", temp, i, j)
                # print("left:", mat[end-offset][i], end-offset, i)
                # print("bottom:", mat[end][end-offset], end, end-offset)
                # print("right:", mat[j][end], j, end)

                # Store top element
                temp = mat[i][j]

                # top = left
                mat[i][j] = mat[end-offset][i] 
                # left = bottom
                mat[end-offset][i] = mat[end][end-offset] 
                # bottom = right
                mat[end][end-offset] = mat[j][end]
                # right = top
                mat[j][end] = temp
    return mat     

if __name__ == "__main__":

    input = [[0,1,2,3,4],
             [5,6,7,8,9],
             [0,1,2,3,4],
             [5,6,7,8,9],
             [0,1,2,3,4]
            ]
    output = rotateMatrix(input)
    for i in range(len(output)):
        print(output[i])
