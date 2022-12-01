import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().rstrip().split())

# 경우의 수를 구하기 위한 배열
lst = [N for N in range (1, N+1)]
for i in list(permutations(lst, M)):
    for k in i:
        print(k, end=" ")
    print("")

''' 자기 자신과 중복되는 얘는 걸러준다.
4 2
1 2 
1 3 
1 4 
2 1 
2 3 
2 4 
3 1 
3 2 
3 4 
4 1 
4 2 
4 3 
'''