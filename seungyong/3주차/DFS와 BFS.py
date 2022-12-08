from collections import deque

def DFS(start):
    print(start, end = ' ')
    visited[start] = True
     
    for v in graph[start]: # start노드와 연결된 노드 중 
        if visited[v] == False: #방문안한 노드 탐색
            DFS(v)

def BFS(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft() 
        print(current, end = ' ')


        for v in graph[current]: # start노드와 연결된 노드 중 
            if visited[v] == False: #방문안한 노드 탐색
                queue.append(v)
                visited[v] = True
    # 1은 2, 3 과 연결되어있고
    # 2는 1, 5
    # 3은 1, 4
    # 4는 3, 5
    # 5는 2, 4 와 연결되어있다.
    # 이 때 시작점이 1이라면 queue의 상태는 다음과 같이 진행된다.
    # BFS(1) -> queue[1] -> popLeft = 1 -> queue[2, 3]    visited[True, True, True, False, False]
    #        -> popLeft = 2 -> queue[3, 5]                visited[True, True, True, False, True]
    #        -> popLeft = 3 -> queue[5, 4]                visited[True, True, True, True, True]
    #        -> popLeft = 5 -> queue[4]                   visited[True, True, True, True, True]
    #        -> popLeft = 4 -> 종료


N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)] # 그래프 선언



for i in range(M): # 그래프 구성(양방향)
    A, B = map(int, input().split()) # A To B
    graph[A].append(B)
    graph[B].append(A)

for g in graph: # 정점 오름차순 정렬
    g.sort()
#print(graph)
visited = [False for i in range(N+1)] 
DFS(V)
visited = [False for i in range(N+1)]
print() 
BFS(V)
