import sys

M, N = map(int, sys.stdin.readline().split())
lst = []

for i in range(M, N):
    if (i == 1):
        continue
    for k in range(2, i):
        if (i % k == 0):
            break
    else:
        lst.append(i)

for i in lst:
    print(i)
