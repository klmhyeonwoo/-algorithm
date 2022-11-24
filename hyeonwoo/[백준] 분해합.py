import sys

N = int(sys.stdin.readline().rstrip())

for i in range (1, N+1):
    answer = 0

    # 자릿수를 더해주는 로직
    littleN = str(i)
    for k in range (len(str(i))):
        answer += int(littleN[k])
    
    numSum = i + answer
    #print(f'numSum : {i} + {answer} = {numSum}')
    if (numSum == N):
        print(i)
        break

    if (i == N):
        print(0)



