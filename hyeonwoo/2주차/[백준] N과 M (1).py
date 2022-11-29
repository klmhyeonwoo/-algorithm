import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().rstrip().split())

# 경우의 수를 구하기 위한 배열
lst = [N for N in range (1, N+1)]
for i in list(permutations(lst, M)):
    for k in i:
        print(k, end=" ")
    print("")