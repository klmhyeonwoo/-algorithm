import sys
from collections import Counter

N = int(sys.stdin.readline())
answer = 1
cnt = 0

while N > 0:
    cnt += N // 5
    N //= 5

print(cnt)

# 0의 개수는 5의 배수일때마다 달라진다.
# https://lucian-blog.tistory.com/84
