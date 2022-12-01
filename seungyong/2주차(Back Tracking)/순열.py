def permutation(size):
    global M
    if size == M:
        for k in lst:
            print(k,end=' ')
        print()
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            lst.append(i)
            permutation(size + 1)
            visited[i] =False
            lst.pop()
    
N, M = map(int, input().split())
lst = []
visited = [False for _ in range(0,N+1)]

permutation(0)
