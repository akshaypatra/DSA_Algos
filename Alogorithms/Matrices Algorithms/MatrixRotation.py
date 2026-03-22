
'''
To rotate an matrix by 90 degree (clockwise)

                0   1   2     --->          0   1   2
            0   00  01  02      90*     0   20  10  00
            1   10  11  12              1   21  11  01
            2   20  21  22              2   22  12  11


Example question : 1886. Determine Whether Matrix Can Be Obtained By Rotation
'''


def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix



'''
Anticlockwise rotation

'''

def rotate_anticlockwise(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each column
    for j in range(n):
        top, bottom = 0, n - 1
        while top < bottom:
            matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
            top += 1
            bottom -= 1

    return matrix