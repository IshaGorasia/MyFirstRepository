a = 7
memoized = [-1 for i in range(a+1)]
def fib(a,memoized) :
    if a == 1 or a== 0:
        memoized[a] = a
        #return a
    if memoized[a] == -1 :
        memoized[a] = fib(a-1,memoized) + fib(a-2,memoized)
    return memoized[a]

print(fib(a,memoized))
