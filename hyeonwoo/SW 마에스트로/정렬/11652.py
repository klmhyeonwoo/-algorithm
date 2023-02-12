import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
lst = Counter(lst)
maxOfNum = 0
maxOfTitle = 1

for i in lst.keys():
    if (lst[i] > maxOfNum):
        maxOfNum = lst[i]
        maxOfTitle = i

print(maxOfTitle)
