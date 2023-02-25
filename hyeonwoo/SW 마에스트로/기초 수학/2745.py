import sys

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(str, sys.stdin.readline().rstrip().split())
answer = 0

for i in range(len(N)-1, -1, -1):  # 4~0 까지 내려오는 반복문
    # print(tmp.index(N[len(N)-1 - i]), B, i, int(B) ** i)
    answer += tmp.index(N[len(N)-1 - i]) * (int(B) ** i)

print(answer)
