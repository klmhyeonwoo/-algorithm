import sys

# 첫 줄에는 미래에서 사용하는 미래의 진법 A와 정이가 사용하는 진법  (모두 2 이상 및 30 이하의 자연수)
# 두번째 줄에는 A진법으로 나타낸 숫자의 자리수 개수 m이 주어진다.
# 세번째 줄에는 A진법을 이루고 있는 숫자 m개가 공백을 구분으로 높은 자릿수부터 차례대로 주어진다.
# 각 숫자는 0이상 A미만임이 보장된다. (0으로 시작하는 경우는 없다)

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

answer = 0
result = []

for i in range(m - 1, -1, -1):
    answer += lst[abs(m - 1 - i)] * (A ** i)

# for i in range (m):
#     answer += lst[i] * (A ** i)

# B진법 로직으로 짜야한다.
while answer != 0:
    result.append(str(answer % B))
    answer //= B

print(" ".join(map(str, result)))
