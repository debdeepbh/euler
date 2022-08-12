maxpalin = 0
for i in range(100,1000):
    for j in range(100, 1000):
        r = i * j
        p = str(int(r))
        if p == p[::-1]:
            print(p)
            maxpalin = max(maxpalin, r)

print('max palindrome', maxpalin)   
