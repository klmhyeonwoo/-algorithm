import sys
from itertools import combinations
from itertools import product

# 몇 번 입력을 받을건지 N에 입력을 받아요
N = int(sys.stdin.readline())

# 0으로 4칸의 배열을 만들어준다 (임시)
S = [[0] for _ in range (N)]

# S 변수에 만들어진 배열에 채워줄거예요
for i in range (N):
    S[i] = list(map(int, sys.stdin.readline().split()))

# N만큼 입력을 받을건데 그에 따른 경우의 수를 repeat 변수에 저장해요
repeat = [x for x in range (0, N)]

# 그리고 이 repeat 변수를 짝수로 나눠주면 스타트와 링크로 나눠지게 돼요
lst = list(combinations(repeat, N//2))

# 차를 저장할 수 있도록 전역 변수에 저장해요
minus = 0

# 여기서부터 본 로직이 시작되어요
for i in range (1, (len(lst) //2) + 1):
    # 전역변수 minus에 담기 위해 temp 변수들을 만들어요
    s_temp = 0
    l_temp = 0
    # minus temp와 전역변수 temp를 비교하면서 최소값을 만들어줄거에요
    minus_temp = 0

    # 스타트는 첫번째부터, 링크는 마지막서부터 서로 계산을 진행해요
    s_data = list(combinations(lst[i-1], 2))
    l_data = list(combinations(lst[-i], 2))

    for x, y in zip(s_data, l_data):
        s_first = x[0]; s_twice = x[1]
        l_first = y[0]; l_twice = y[1]
        # 거꾸로 경우의 수도 고려를 해주는 로직이에요
        s_temp += S[s_first][s_twice]; s_temp += S[s_twice][s_first]
        l_temp += S[l_first][l_twice]; l_temp += S[l_twice][l_first]
    # 절댓값 처리로 스타트와 링크의 차이를 저장해주고
    minus_temp = abs(s_temp - l_temp)

    # 첫번째 시도 일 경우 그냥 저장,
    if (i == 1):
        minus = minus_temp
    # 그게 아니면 minus_temp 변수와 minus 변수의 비교를 통해 최솟값을 최신화시켜요
    if (minus >= minus_temp):
        minus = minus_temp

print(minus)




