import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    name, kor, eng, math = map(str, sys.stdin.readline().split())

    lst.append((name, int(kor), int(eng), int(math)))

lst.sort(key=lambda lst: (-lst[1], lst[2], -lst[3], lst[0]))

for i in lst:
    print(i[0])
