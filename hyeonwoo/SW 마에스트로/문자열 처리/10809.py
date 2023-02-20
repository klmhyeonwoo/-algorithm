import sys

word = sys.stdin.readline().rstrip()
newDict = {}

for i in range(len(word)):
    if (word[i] in newDict):
        continue
    else:
        newDict[word[i]] = i

for i in range(97, 123):
    if (chr(i) in newDict):
        print(newDict[chr(i)], end=" ")
    else:
        print(-1, end=" ")
