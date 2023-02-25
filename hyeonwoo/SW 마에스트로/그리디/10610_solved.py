import sys

N = sys.stdin.readline().rstrip()

if "0" not in N:  # 3의 배수이면서, 10의 배수이기때문에 0이 없으면 그냥 -1을 출력
    print(-1)
else:
    result = 0
    for i in range(len(N)):
        result += int(N[i])

    if (result % 3 != 0):
        print(-1)
    else:
        NT = sorted(N, reverse=True)
        answer = "".join(NT)
        print(answer)
