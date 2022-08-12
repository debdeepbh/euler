def partition(n):
    print('n', n)
    if n==1:
        return [[1]]
    # elif n==2:
    #     return [[1,1], [2]]
    # elif n==3:
    #     return [[1,1,1], [2,1], [3]]
    # elif n==4:
    #     return [[1,1,1,1], [2,1,1], [3,1], [2,2], [4]]
    else:
        for i in range(1,n-i):
            pnew = partition(n-i) + [[i]]
        return pnew



n = 2
print(partition(n))

