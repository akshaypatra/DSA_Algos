
'''
Transpose of matrix using extra space 

'''
def transpose(mat):
    rows = len(mat)             
    cols = len(mat[0])         

    # Create a result matrix of size
    # cols x rows for the transpose
    tMat = [[0 for _ in range(rows)] for _ in range(cols)]

    # Fill the transposed matrix by
    # swapping rows with columns
    for i in range(rows):
        for j in range(cols):
            
            # Assign transposed value
            tMat[j][i] = mat[i][j]

    return tMat

'''
Transpose of matrix (in place)
'''

def transposeInplace(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix



if __name__ == "__main__":
    mat = [[1, 1, 1, 1],[2, 2, 2, 2],[3, 3, 3, 3], [4, 4, 4, 4]]

    res = transpose(mat)
    res2= transposeInplace(mat)

    print("Extra space :" )
    for row in res:
        for elem in row:
            print(elem, end=' ')
        print()

    print("In place :")
    for row in res:
        for elem in row:
            print(elem, end=' ')
        print()