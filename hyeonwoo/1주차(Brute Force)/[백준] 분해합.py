import sys

# N 입력
N = int(sys.stdin.readline().rstrip())

for i in range (1, N+1):
    answer = 0

    # 자릿수를 더해주는 로직
    littleN = str(i)
    # 198 => 1 + 9 + 8 = 18
    for k in range (len(str(i))):
        answer += int(littleN[k])
    # answer = 18
    # i = 198
    # numsum = 216
    numSum = i + answer
    #print(f'numSum : {i} + {answer} = {numSum}')
    if (numSum == N):
        print(i)
        break

    if (i == N):
        print(0)



