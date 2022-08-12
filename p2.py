def evenfibsum(n):
    old1 = 1
    old2 = 2

    sum = 2
    while old2 < n:
        currnum = old1 + old2
        print(currnum)
        if (currnum % 2 == 0) and currnum < n:
            sum += currnum

        old1 = old2
        old2 = currnum
    return sum

# n = 1e2
n = 4e6
print('sum',evenfibsum(n))
