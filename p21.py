def divsum(n):
    sum = 1
    for i in range(2,n):
        if n % i == 0:
                sum += i
    return sum

print(divsum(220))
print(divsum(284))

# N = 100
N = 10000
nums = list(range(1, N+1))
yes = []

while nums!=[]:
    val = nums.pop(0)
    ss = divsum(val)
    if ss <= N:
        if divsum(ss) == val:
            if ss != val:
                yes.append(val)
                yes.append(ss)
                # print('yes', val)
        try:
            nums.remove(ss)
        except Exception as e:
            # raise e
            pass
print(yes)
print(sum(yes))


    
    

