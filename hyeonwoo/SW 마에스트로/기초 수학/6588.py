import sys

check = [True for _ in range(100_000_1)]

# 100_001 ** 0.5 + 1
for i in range(2, 1001):
    if (check[i]):
        for k in range(i * 2, 100_000_1, i):
            check[k] = False

while True:
    N = int(sys.stdin.readline())
    if (N == 0):
        break
    for i in range(3, len(check)):
        if (check[i]):
            if (check[N-i]):
                print(f'{N} = {i} + {N-i}')
                break

# https://newl.yammyblock.com/43 (가장 쉬운 풀이)
# https://velog.io/@dding_ji/%EB%B0%B1%EC%A4%80-6588.-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-Python-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
