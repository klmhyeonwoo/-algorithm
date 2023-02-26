import sys

N, M, K = map(int, sys.stdin.readline().split())
count = 0

# 6 3 2
# 4 2 2 - 1
# 2 1 2 - 2

while True:
    if (N - 2 < K and M - 1 < K):
        break
    elif (N == 0 or M == 0):
        break
    else:
        N -= 2
        M -= 1
        count += 1

# 10 10 5
# 8 9 5 - 1
# 7 8 5 - 2
# 5 7 5 - 3

# 6 3 2
# 4 2 2 - 1
# 2 1 2 - 2

# 6 10 3
# 4 9 3 - 1
# 2 8 3 - 2
# 0 7 3 - 3

print(count)
