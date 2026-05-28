import numpy as np

def matrix_transpose(A):
    n = len(A)      # rows
    m = len(A[0])   # cols

    # Create empty M×N matrix
    B = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    b=np.array(B)

    return b
        
    pass
