def factor(n):
    d = 2
    maxfac = d

    while n > 2:
        if n % d == 0:
            maxfac = max(maxfac, d)
            # divide out the factor
            n = n/d
        d += 1

    return maxfac  

# n = 13195
n = 600851475143
print(factor(n))

