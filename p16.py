def twopow(n):
    """TODO: Docstring for twopow.

    :n: TODO
    :returns: TODO

    """
    digits = [2]
    for i in range(1,n):
        digits = [d*2 for d in digits]
        # print('digits',digits)
        # carry, stored in the reverse order
        for j in range(len(digits)):
            val = digits[j]
            rem = val % 10
            carry = val // 10
            # print('carry', carry)
            digits[j] = rem
            if j==len(digits)-1:
                # print('digits before append',digits)
                if carry!=0:
                    digits.append(carry)
                # print('digits after append',digits)
            else:
                digits[j+1] += carry

    return digits[::-1]

# n = 10
n = 1000
# print(twopow(n))
print(sum(twopow(n)))


