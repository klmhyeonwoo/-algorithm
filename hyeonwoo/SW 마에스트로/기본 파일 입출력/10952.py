import sys

while (1):
    a, b = map(int, sys.stdin.readline().split())
    if (a == 0 and b == 0):
        print(a, b)
        break
    else:
        print(a + b)
