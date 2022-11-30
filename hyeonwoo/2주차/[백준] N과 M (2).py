import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())

# 경우의 수를 구하기 위한 배열
lst = [N for N in range (1, N+1)]
for i in list(combinations(lst, M)):
    for k in i:
        print(k, end=" ")
    print("")

''' 중복을 걸러주면서, 순서에 의미가 없다 (= 같은 값이 뽑히면 같은 경우의 수로 판단)
4 2
1 2 
1 3 
1 4 
2 3 
2 4 
3 4 
'''