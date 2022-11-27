import sys
# Test case의 수 T가 주어진다.
t = int(sys.stdin.readline()) 

for _ in range(t): # T만큼 반복을 시켜줄거예요
    floor = int(sys.stdin.readline()) # 층을 입력
    num = int(sys.stdin.readline()) # 호수를 입력
    f0 = [x for x in range (1, num + 1)] # 0층을 모델링 해줘요
    # print("f0", f0), 매 순간 0층이 출력될겁니다.
    for k in range(floor): # 층 만큼 반복을 시켜줍니다.
        for i in range (1, num): # 층 안에서 호수 만큼을 반복해야하는데,
            f0[i] += f0[i-1] # 각 층의 호수를 결정 할 때, 
    print(f0) # f0을 새롭게 구성을 시켜준다.
