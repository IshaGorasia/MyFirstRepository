def lcs(x,y) :
    m = len(x)
    n = len(y)
    
    # Declare the memoized array
    L = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1) :
        for j in range(1,n+1) :
            if x[i-1] == y[j-1] :
                L[i][j] = L[i-1][j-1]+1
            else :
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[m][n]


x = "ABCD"
y = "BD"
print(lcs(x,y))
