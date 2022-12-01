def permutation(level):
    global M
    if len(lst) == M: # 중단조건 M개 고르면 끝
        for k in lst:
            print(k,end=' ')
        print()
        return

    for i in range(level, N + 1):
        if visited[i] == False:
            visited[i] = True
            lst.append(i)
            permutation(i + 1)
            visited[i] =False
            lst.pop()
 
N, M = map(int, input().split())
lst = []
visited = [False for _ in range(0,N+1)] # 0 ~ N

permutation(1)
