import sys
from itertools import combinations

T = int(sys.stdin.readline())

for i in range(T):
    answer = 0
    num = list(map(int, sys.stdin.readline().split()))
    num.pop(0)
    for lst in list(combinations(num, 2)):
        A, B = map(int, lst)
        a, b = A, B
        while (b != 0):
            a = a % b
            a, b = b, a
        # print(A, B, a)
        answer += a
    print(answer)
