import sys
from itertools import permutations

N = sys.stdin.readline().rstrip()
lst = []

for i in N:
    lst.append(i)

result = list(permutations(lst, len(N)))
result.sort(key=lambda result: result)
result.reverse()

for i in result:
    if (int("".join(i)) % 30 == 0):
        print(int("".join(i)))
        break
