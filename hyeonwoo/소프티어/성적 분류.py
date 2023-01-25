import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
S = list(sys.stdin.readline().rstrip().split())

for i in range(K):
    avg = 0
    A, B = map(int, sys.stdin.readline().rstrip().split())

    section = S[A-1:B]
    for i in section:
        avg += int(i)
    print(avg)
    print(f'{avg / len(section):.2f}')
