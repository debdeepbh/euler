def npaths(n):
    # 2n moves, exactly n Rs and n Ds
    # 2n choose n   = (2n)!/n! n! = 2n (2n-1) ... (n+1)/n! = (2n-0)/(n-0) ( 2n-1)/(n-1) (2n-2)/(n-2) ... (n+1)/1
    prod = 1
    for i in range(0,n):
        prod *= (2*n - i)/(n -i)
    return prod

# n = 2
n = 20
print(npaths(n))

