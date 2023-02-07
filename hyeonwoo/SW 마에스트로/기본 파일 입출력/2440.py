import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    for k in range(0, i):
        print("*", end="")
    print()
