import sys

T = int(sys.stdin.readline())

for _ in range (T):
    # 층고에 대한 높이를 입력 받습니다
    floor = int(sys.stdin.readline())
    # 호수에 대한 내용을 입력 받습니다
    num = int(sys.stdin.readline())
    # f0부터 계산을 차곡차곡 해줘야하기 때문에 기준이 되는 f0을 만들어줍니다
    # f0 = [1, 2, 3, ...]
    f0 = [x for x in range (1, num+1)]
    # 층고의 높이 만큼 반복을 해주고,
    for k in range (floor):
        # 또 그 안에서 호수만큼의 반복을 수행해줍니다
        # 각 층수의 인원을 변경해주기 위해서, 새로운 호수를 만날 때마다 그 이전의 값을 더해줌으로써 새롭게 변경합니다.
        for z in range (1, num):
            f0[z] += f0[z-1]
    print(f0[-1])
        

