# Kaatsuba algorithm - Divide & conquer

def karatsuba(x,y) :
    # base case - atomic multiplication
    if x<10 or y<10 :
        return x*y
    m = max(len(str(x)),len(str(y)))
    if m%2 != 0 :  # if it is odd
        m -= 1
        # converting odd to the even no

    a,b = divmod(x,10**int(m/2))
    c,d = divmod(y,10**int(m/2))

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)

    ad_bc = karatsuba((a+b),(c+d)) - ac - bd

    return ((ac*(10**m))+(ad_bc*(10**int(m/2)))+bd) #karatsuba equation


x = int(input('Enter Number 1: '))
y = int(input('Enter Number 2: '))

print(karatsuba(x,y))
