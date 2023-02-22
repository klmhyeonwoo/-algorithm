import sys

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, sys.stdin.readline().split())
answer = ''

while (N != 0):
    answer += str(tmp[N % B])
    N = N // B

print(answer[::-1])

# https: // duwjdtn11.tistory.com/486
