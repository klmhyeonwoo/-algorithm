import sys

num = int(sys.stdin.readline())

numSet = list(sys.stdin.readline().rstrip())
answer = 0

for i in range(num):
    answer += int(numSet[i])

print(answer)
