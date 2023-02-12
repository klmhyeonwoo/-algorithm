import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

lst.sort()

lst.sort(key=lambda lst: (lst[1]))

for i in lst:
    print(i[0], i[1])
