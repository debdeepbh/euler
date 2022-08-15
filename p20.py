def facdigsum(n):
    digits = [1]
    for i in range(2,n+1):
        digits = [d*i for d in digits]
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
                    # if carry > 9:
                        # if more than one digit
                        chars = [int(s) for s in str(carry)]
                        digits = digits + chars[::-1]
                    # else:
                    #     digits.append(carry)

            else:
                digits[j+1] += carry

    return digits[::-1]

# n = 10
# n = 15
n = 100
fac = facdigsum(n)
print('fac', fac)
print(sum(fac))


