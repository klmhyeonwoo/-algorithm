import sys
from itertools import combinations_with_replacement


N, M = map(int, sys.stdin.readline().rstrip().split())

# 경우의 수를 구하기 위한 배열
lst = [N for N in range (1, N+1)]
for i in list(combinations_with_replacement(lst, M)):
    for k in i:
        print(k, end=" ")
    print("")

''' 숫자의 거꾸로 된 중복만을 제외하고, 그 외에 중복을 허용하는 조합
4 2
1 1 
1 2 
1 3 
1 4 
2 2 
2 3 
2 4 
3 3 
3 4 
4 4
'''