import sys

N = int(sys.stdin.readline())
lst = [0] * 10001

for i in range(N):
    number = int(sys.stdin.readline())
    lst[number] += 1

for i in range(10001):
    if (lst[i] != 0):
        for k in range(lst[i]):
            print(i)
