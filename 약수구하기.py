import sys

N, K = sys.stdin.readline().rstrip().split()

N = int(N)
K = int(K)

for i in range (1, N+1):
    if (N % i == 0):
        K -= 1
        if (K == 0):
            print(i)
            break
else:
    print(0)