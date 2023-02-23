import sys

N = int(sys.stdin.readline())
res = ''

if not N:
    print(0)
    exit()

while (N):
    if (N % -2):
        N = N // -2 + 1
        res = '1' + res
    else:
        N = N // -2
        res = '0' + res

print(res)

# https://suri78.tistory.com/119
