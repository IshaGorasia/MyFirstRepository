import numpy as np

def split(A,n):

    mid = int(n/2)

    A11 = A[:mid,:mid]
    A12 = A[:mid,mid:]
    A21 = A[mid:,:mid]
    A22 = A[mid:, mid:]
    return A11,A12,A21,A22

def strassen(x, y):

    if len(x) == 1:
        return x * y

    a, b, c, d = split(x,len(x))
    e, f, g, h = split(y,len(y))

    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    c11 = np.array(p5) + np.array(p4) - np.array(p2) + np.array(p6)
    c12 = np.array(p1) + np.array(p2)
    c21 = np.array(p3) + np.array(p4)
    c22 = np.array(p1) + np.array(p5) - np.array(p3) - np.array(p7)

    c = np.array([[c11],[c12],[c21],[c22]])
    return c

    # First matrix. M is a list
M = np.array([[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]])

# Second matrix. N is a list
N = np.array([[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]])

# Call matrix_multiplication function
ans = strassen(M, N)
#printing the numpy 2D-Array
print("\nThe Numpy 2D-Array is:")
for i in ans:
    for j in i:
        print(j, end=" ")
    print()
