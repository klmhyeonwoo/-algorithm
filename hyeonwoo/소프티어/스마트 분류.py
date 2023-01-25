import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
TC = list(sys.stdin.readline().rstrip())

cnt = 0

for i in range(N):
    if (TC[i] == "P"):
        for j in range(i-K, i+K+1):
            if j < 0 or j >= N:
                continue
            elif TC[j] == "H":
                cnt += 1
                TC[j] = "A"
                break

print(cnt)
