import sys

A, B = map(int, sys.stdin.readline().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

print(a)
print(A * B // a)

# https://suri78.tistory.com/36
