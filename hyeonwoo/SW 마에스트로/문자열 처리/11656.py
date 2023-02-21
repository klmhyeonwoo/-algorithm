import sys

word = sys.stdin.readline().rstrip()
lst = []

for i in range(len(word)):
    lst.append(word[i:])

lst.sort()

for i in lst:
    print(i)
