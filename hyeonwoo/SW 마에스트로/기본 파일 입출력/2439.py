import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    for k in range(1, i):
        print(" ", end="")
    for k in range(0, abs(i-N-1)):
        print("*", end="")
    print()
