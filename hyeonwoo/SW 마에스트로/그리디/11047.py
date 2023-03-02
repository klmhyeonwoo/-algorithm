import sys

N, K = map(int, sys.stdin.readline().split())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.reverse()

count = 0
minimize = 999

for i in lst:
    if (K // i != 0):
        minimize = min(minimize, K // i)
        count += K // i
        K = K % i

print(count)
