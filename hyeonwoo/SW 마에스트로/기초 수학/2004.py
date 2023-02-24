import sys

N, M = map(int, sys.stdin.readline().split())


def count_number(n, k):
    count = 0
    while n > 0:
        count += n // k
        n //= k

    return count


# N > M 이라는 조건이 들어있음
# 끝자리가 0으로 끝난다는 것은 10의 배수, 10은 2와 5의 약수를 가지고 있다.
# 2와 5의 쌍을 찾아주고 이를 맞춰줘야함
five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)

# https://deok2kim.tistory.com/195
