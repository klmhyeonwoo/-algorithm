import sys
from itertools import permutations


def solution(rail):
    total = 0
    cnt = 0

    for i in range(K):
        bucket = 0

        while True:
            bucket += rail[cnt]
            cnt = (cnt + 1) % N
            if (bucket + rail[cnt] > M):
                break
        total += bucket

    return total


N, M, K = map(int, sys.stdin.readline().rstrip().split())
W = list(map(int, sys.stdin.readline().rstrip().split()))

rails = list(permutations(W, N))
answer = []

for rail in rails:
    answer.append(solution(rail))

print(min(answer))
