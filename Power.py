def power(x,n) :
    if n==0 :
        return 1
    elif int(n%2)==0 :
        return (power(x,int(n/2))*power(x,int(n/2)))
    else :
        return (x*power(x,int(n/2))*power(x,int(n/2)))

n = 5
x = 2
print(power(x,n))


# optimized solution
def power2(x,n) :
    if n==0 :
        return 1
    flag = power(x,int(n/2))
    if int(n%2)==0 :
        return (flag*flag)
    else :
        return (x*flag*flag)

n = 5
x = 2
print(power2(x,n))
