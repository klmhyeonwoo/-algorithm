import sys

# 세로가 3 이상과 미만일 때 경우가 달라진다.

R, C = map(int, sys.stdin.readline().split())  # R은 행(가로), C는 열(새로)

lst = []

for i in range(R):
    lst.append(list(map(int, sys.stdin.readline().split())))

if (R % 2 == 1):  # R이 홀수 일 경우, ㄹ자를 그리며 모두 방문할 수 있다.
    print(("R" * (C-1) + "D" + "L" * (C-1) + "D") * (R // 2) + "R" * (C-1))
elif (C % 2 == 1):  # L이 홀수 일 경우, 뒤집힌 ㄹ자를 그리며 모두 방문할 수 있다.
    print(("D" * (R-1) + "R" + "U" * (R-1) + "R") * (C // 2) + "D" * (R-1))
elif (R % 2 == 0 and C % 2 == 0):  # R과 L이 모두 짝수일 경우 모든 칸을 방문할 수 없다.
    low = 1000  # 최대 기쁨은 1000으로 문제에서 제한되었다.
    position = [-1, -1]

    for i in range(R):
        if (i % 2 == 0):  # 짝수 행이라면 아래 코드를 실행한다.
            # 홀수 칸만 지정
            for j in range(1, C, 2):
                if (low > lst[i][j]):
                    low = lst[i][j]
                    position = [i, j]
        else:  # 홀수 행이라면 아래 코드를 실행한다.
            # 짝수 칸만 지정
            for j in range(0, C, 2):
                if (low > lst[i][j]):
                    low = lst[i][j]
                    position = [i, j]

    # 한칸을 제외하면, 홀수로 처리가 되기 때문에 모든 칸수를 방문을 할 수 있다.
    res = ('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (position[1] // 2)

    # 홀수를 짝수로 만들어준다.
    x = 2 * (position[1] // 2)
    # y는 무조건 0, 위에서 시작하기 때문이다.
    y = 0
    # 홀수를 짝수로 만들어준다음, 무조건 오른쪽으로 1칸 이동해야하는 과정이 있기 때문에 xbound에 1을 더해준다.
    xbound = 2 * (position[1] // 2) + 1

    # x와 xbound가 같고, y가 맨 밑칸까지 갔다면 멈춤
    while x != xbound or y != R-1:
        # x가 xbound보다 왼쪽에 있고, [y, xbound]의 position의 값이 틀리다면 오른쪽으로 이동
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        # x가 xbound랑 값이 같으며, [y, xbound]와 position의 값이 틀리다면 왼쪽으로 이동
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += "L"

        if (y != R - 1):
            y += 1
            res += "D"

        # print(x, xbound, [y, xbound], position, res)

    # x : 0, xbound: 1 | y, xbound : 0,1 | position : 0,1
    # x : 0, xbound: 1 | y, xbound : 0,1 | position : 0,1 => (D) x : 0, xbound: 1 | y, xbound : 1,1 | position : 0,1
    # x : 0, xbound: 1 | y, xbound : 1,1 | position : 0,1 => (R, D) x : 1, xbound: 1 | y, xbound : 2,1 | position : 0,1
    # x : 1, xbound: 1 | y, xbound : 2,1 | position : 0,1 => (L, D) x : 0, xbound: 1 | y, xbound : 3,1 | position : 0,1
    # x : 0, xbound: 1 | y, xbound : 3,1 | position : 0,1

    res += ('R' + 'U' * (R-1) + 'R' + 'D' * (R-1)) * \
        ((C - position[1] - 1) // 2)
    print(res)


# https://seungyong20.tistory.com/39
