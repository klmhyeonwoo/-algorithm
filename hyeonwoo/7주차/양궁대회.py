from itertools import combinations_with_replacement


def solution(n, info):
    LION_LST = [-1]
    LION_MAX_GAP = -1
    target = [i for i in range(1, 11)]

    for lst in combinations_with_replacement(range(11), n):
        LION = [0 for i in range(11, 0, -1)]

        for i in lst:
            LION[10 - i] += 1

        APEACH_NUM = 0
        LION_NUM = 0

        for k in range(11):
            if info[k] == LION[k] == 0:
                continue  # 0의 값이니까
            elif (info[k] >= LION[k]):
                APEACH_NUM += 10 - k
            else:
                LION_NUM += 10 - k

        if (LION_NUM > APEACH_NUM):
            GAP = LION_NUM - APEACH_NUM
            if (GAP > LION_MAX_GAP):
                LION_MAX_GAP = GAP
                LION_LST = LION
    return (LION_LST)


# 어피치가 화살 N발을 다 쏜 후에 라이언이 화살 N발을 쏜다.
# 가장 작은 원의 과녁 점수는 10점이고, 가장 큰 원의 바깥 쪽은 과녁 점수가 0점
# K는 1부터 10사이의 자연수
# 더 많은 화살을 K점에 맞힌 선수가 K점을 가져가는 시스템
# 단, A = B 일 경우에는 어피치가 K점을 가져가게 된다.

# 최종 점수가 더 높은 선수를 우승자로 결정, 단 최종점수가 같을 경우 어피치를 우승자로 결정한다.
# 상황은 어피치가 화살 N발을 다 쏜 후 이고, 라이언이 화살을 쏠 차례이다.

# 문제의 요지는 라이언이 어피치를 가장 큰 점수 차이로 이기기 위해서 N발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 한다.

# 화살의 개수를 담은 자연수 N, 어피치가 맞힌 과녁의 점수의 개수를 순서대로 담은 정수 배열 Info
# 만약 라이언이 우승할 수 없거나, 비기는 경우에는 -1을 리턴
