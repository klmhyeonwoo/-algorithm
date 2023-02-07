import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    for a in range(1, i):
        print(" ", end="")
    for b in range(N * 2 + 1, i + i, -1):
        print("*", end="")
    print()

for i in range(N-1, 0, -1):
    for a in range(i, 1, -1):
        print(" ", end="")
    for b in range(i + i, N*2+1):
        print("*", end="")
    print()
