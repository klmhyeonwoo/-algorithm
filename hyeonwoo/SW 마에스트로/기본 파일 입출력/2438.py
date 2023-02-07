import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):  # 1~5
    for k in range(0, i):  # 0~i
        print("*", end="")
    print()
