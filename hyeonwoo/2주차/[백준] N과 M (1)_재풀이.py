import sys

def permutation(size, M):
    if (size == M):
        for i in lst:
            print(i, end=" ")
        print()
        return
    
    for k in range (1, N+1):
        if (visited[k] == False):
            visited[k] = True
            lst.append(k)
            permutation(size + 1, M)
            visited[k] = False
            lst.pop()

N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [False for _ in range (0, N+1)]
lst = []

permutation(0, M)
