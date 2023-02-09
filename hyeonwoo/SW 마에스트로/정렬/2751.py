import sys

N = int(sys.stdin.readline())
LIST = []

for i in range(N):
    LIST.append(int(sys.stdin.readline()))

LIST.sort()

for i in LIST:
    print(i)
