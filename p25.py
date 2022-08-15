import copy
def sumbydigit(ls1, ls2):
    sz = len(ls1)
    nn = len(ls2)
    for i, digit in enumerate(ls2):
        if i < sz:
            b = ls1[i]
        else:
            b = 0
        ls2[i] += b

    for i in range(nn):
        digit = ls2[i]
        if digit > 9:
            ls2[i] = digit % 10
            carry = digit // 10
            if i != nn-1:
                ls2[i+1] += carry
            else:
                ls2.append(carry)


old1 = [1]
old2 = [1]

N = 1000
# N = 4
# N = 3
ind = 2
while len(old2) < N:
    temp = copy.deepcopy(old2)
    # print(old2)
    sumbydigit(old1, old2)
    old1 = temp
    ind += 1
    # print(old2)

print(ind)

