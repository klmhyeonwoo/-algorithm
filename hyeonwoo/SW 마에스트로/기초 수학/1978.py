import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(N):
    count += 1
    # print(lst[i], end=" ")
    if (lst[i] == 1):
        count -= 1
    for k in range(2, lst[i]):
        # print(k, end=" ")
        if (lst[i] % k == 0):
            count -= 1
            break
    # print()

print(count)
