# 시계방향이라면, 시계 반대방향으로 생각하고 해당 값을 끌고온다는 느낌으로 로직을 작성할 것!

def solution(rows, columns, queries):
    array = []
    temp = []
    answer = []

    # 행렬을 먼저 만들어줍시다.
    for i in range(1, rows * columns + 1):
        temp.append(i)
        if (len(temp) % columns == 0):
            array.append(temp)
            temp = []

    for x1, y1, x2, y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        # x1 : 2, x2 : 5 (2, 3, 4)

        # 왼쪽 세로
        for k in range(x1-1, x2-1):
            lotation = array[k+1][y1-1]
            array[k][y1-1] = lotation
            mini = min(mini, lotation)

        # 하단 가로
        for k in range(y1-1, y2-1):
            lotation = array[x2-1][k+1]
            array[x2-1][k] = lotation
            mini = min(mini, lotation)

        # 오른쪽 세로
        for k in range(x2-1, x1-1, -1):
            lotation = array[k-1][y2-1]
            array[k][y2-1] = lotation
            mini = min(mini, lotation)

        # 상단 가로
        for k in range(y2-1, y1-1, -1):
            lotation = array[x1-1][k-1]
            array[x1-1][k] = lotation
            mini = min(mini, lotation)

        array[x1-1][y1] = tmp
        answer.append(mini)

    # print(array)

    return answer

# 테스트 코드
# print(solution(6, 6, [[2, 2, 5, 4]]))

# (2, 2) -> (5, 4)
# (2, 3, 4 x축으로 ) - (2, 3, 4, 5) -> (4, 3, 2) -> (5, 4, 3, 2)
