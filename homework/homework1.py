def modExp(b, n, m):
    #FIXME: IMPLEMENT THIS METHOD
    i = 0
    ans = b
    while i < n - 1:
        ans = ans * b
        i = i + 1
    ans = ans%m
    print("Answer: ", ans)
    
modExp(3,644,645)



def bezoutCoeffs(a, b):
    x = 0
    y = 1
    u = 1
    v = 0
    swapped = False
    if a < b:
        swapped = True
        holder = a
        a = b
        b = holder
    
    while a != 0:
        quotient = b//a
        remainder = b%a
        m = x - u * quotient
        n = y - v * quotient
        b = a
        a = remainder
        x = u
        y = v
        u = m
        v = n
    gcd = b
    if swapped == True:
        holder = x
        x = y
        y = holder
    print("(%s, %s)" % (x, y))
    
bezoutCoeffs(414, 662)



def gcd(a,b):
    #FIXME: IMPLEMENT THIS METHOD
    i=1
    compTo = 0
    gcdAns = 0
    if a < b:
        compTo = a
    else:
        compTo = b
        
    while(i < compTo):
        if (a%i == 0) & (b%i == 0):
            gcdAns = i
        i += 1
    
    print("GCD: ", gcdAns)

gcd(414, 662)