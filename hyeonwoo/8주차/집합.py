import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

newLst = [[i] for i in range(0, N+1)]

a = [1, 2]
b = [3, 4]

for i in range(M):
    tempA = []
    tempB = []
    command, a, b = map(int, sys.stdin.readline().rstrip().split())
    if (command == 0):  # command가 0일 때의 로직
        tempA = newLst[a].copy()
        tempB = newLst[b].copy()
        for lst in newLst:
            if (a in lst or b in lst):
                newLst[a].extend(tempB)
                newLst[b].extend(tempA)
                break
        print(newLst)

    if (command == 1):  # command가 1일 때의 로직
        for lst in newLst:
            if (a in lst and b in lst):
                print("YES")
                break
        else:
            print("NO")

# [1, 3]
# NO
# [1, 7]
# NO
# [3, 7]
# [4, 2]
# [1, 1]
