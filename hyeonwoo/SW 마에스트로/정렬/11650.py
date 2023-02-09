import sys

N = int(sys.stdin.readline())
XY = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    XY.append((x, y))

XY.sort()

for i in range(0, len(XY)):
    print(XY[i][0], XY[i][1])
