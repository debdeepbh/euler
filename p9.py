n = 1000
for a in range(1,n+1):
    bpc = n - a
    for b in range(1, bpc):
        c = bpc - b
        if a**2 + b**2 == c**2:
            print('abc', a, b, c)
            print('prod', a*b*c)
