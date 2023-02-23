import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.reverse()

ten = 0
for i in range(m):
    ten += arr[i] * (a ** i)

result = []
while ten != 0:
    result.append(ten % b)
    ten //= b

print(' '.join(map(str, result[::-1])))
