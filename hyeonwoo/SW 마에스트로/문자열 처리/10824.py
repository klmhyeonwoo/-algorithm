import sys

a, b, c, d = map(str, sys.stdin.readline().split())

first = int(a + b)
second = int(c + d)

print(first + second)
