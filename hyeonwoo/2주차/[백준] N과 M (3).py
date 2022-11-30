import sys
from itertools import product

N, M = map(int, sys.stdin.readline().rstrip().split())

# 경우의 수를 구하기 위한 배열
lst = [N for N in range (1, N+1)]
for i in list(product(lst, repeat=M)):
    for k in i:
        print(k, end=" ")
    print("")

''' 모든 중복을 허용하는 순열
4 2
1 1 
1 2 
1 3 
1 4 
2 1 
2 2 
2 3 
2 4 
3 1 
3 2 
3 3 
3 4 
4 1 
4 2 
4 3 
4 4 
'''