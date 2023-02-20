import sys

word = sys.stdin.readline().rstrip()
newDict = {}

for i in word:
    if (i in newDict):
        newDict[i] += 1
    else:
        newDict[i] = 1

for i in range(97, 123):
    if (chr(i) in newDict):
        print(newDict[chr(i)], end=" ")
    else:
        print(0, end=" ")
