import sys

try:
    while (1):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
except:
    exit()
