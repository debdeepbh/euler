def checkprime(n):
    for d in range(2,n):
        if n % d == 0:
            return 1 # not prime
    return n


# prod of all prime numbers upto n
def prodprime(n):
    prod = 1
    for i in range(2,n+1):
        cp = checkprime(i)
        if cp == i:
            print(i)
            prod *= i
    return prod


# n = 13195
# n = 600851475143
n = 10
# print(checkprime(n))
print(prodprime(n))

