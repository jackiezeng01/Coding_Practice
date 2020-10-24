# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

def zeroMatrix(mat):
    rows, cols = len(mat), len(mat[0])

    # Arrays to store the state of rows and cols
    zero_rows = [False]*(rows)
    zero_cols = [False]*(cols)

    # Loop through all elements of array and locate zeros
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    # Make columns zero
    for col in zero_cols:
        if col == True:
            for x in range(rows):
                mat[x][col] = 0

    # Make rows zero
    for row in zero_rows:
        if row == True:
            for y in range(cols):
                mat[row][y] = 0

    return mat

if __name__ == "__main__":
    input = [[1,1,1,1,1,1],
             [1,1,1,1,1,1],
             [1,0,1,1,1,1],
             [1,1,1,1,1,1],
            ]
    output = zeroMatrix(input)


    for i in range(len(input)):
        print(output[i])
