from itertools import permutations

ls = list(range(10))

stop = 1e6
i = 1
for p in permutations(ls):
    if i == stop:
        print(p)
    i += 1

