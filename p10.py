# didn't work, use seive of eratosthenis
def checkprime(n):
    # print('num', n)
    d = 2
    while d < n**0.5:
        if n % d == 0:
            return 0
        d +=1 
    # print(n, 'is prime')
    return n
def sumprimebelow(n):
    sump = 2
    for i in range(3, n):
        sump += checkprime(i)
        # print('sump', sump)
    return sump

# n = 10
n = int(2e6)
print(sumprimebelow(n))

