import sys

N = int(sys.stdin.readline())

for i in range(1, 2 * N // 2 + 1):
    for a in range(0, i):
        print("*", end="")
    for b in range(2 * N, i + i, -1):
        print(" ", end="")
    for c in range(0, i):
        print("*", end="")
    print()
for i in range(2 * N // 2 - 1, 0, -1):
    for a_1 in range(i, 0, -1):
        print("*", end="")
    for b_1 in range(2 * N, i + i, -1):
        print(" ", end="")
    for c_1 in range(i, 0, -1):
        print("*", end="")
    print()
