import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    for a in range(N, i, -1):
        print(" ", end="")
    for b in range(0, i):
        print("* ", end="")
    print()
