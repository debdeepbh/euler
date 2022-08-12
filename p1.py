def mult(n):
    """

    :n: TODO
    :returns: TODO

    """
    sum = 0
    for i in range(1,n):
        if i % 3 == 0:
            print(i)
            sum += i
        elif i % 5 == 0:
            print(i)
            sum += i

    return sum

print(mult(1000)) 
