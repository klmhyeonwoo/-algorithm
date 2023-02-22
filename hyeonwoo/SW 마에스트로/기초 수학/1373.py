import sys

tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = sys.stdin.readline().rstrip()
answer = 0
result = ''

# 10진수로 먼저 변환
for i in range(len(N)-1, -1, -1):
    answer += tmp.index(N[len(N)-1-i]) * (2 ** i)

# 8진수로 변환

while (answer != 0):
    result += tmp[answer % 8]
    answer = answer // 8

print(result[::-1])
