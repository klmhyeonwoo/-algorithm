dx = [0,1,0,-1] # 위 오 아 왼
dy = [-1,0,1,0]


def DFS(start):
    global count
    count += 1

    #print(start, end = ' ')
    visited[start] = True
     
    for v in graph[start]: # start노드와 연결된 노드 중 
        if visited[v] == False: #방문안한 노드 탐색
            DFS(v)


N = int(input()) # 컴퓨터 개수
M = int(input()) # 컴퓨터 쌍의 개수

graph = [[] for i in range(N+1)] # 그래프 선언(1번 ~ N번 컴퓨터)
visited = [False for i in range(N+1)] 


for i in range(M): # 그래프 구성(양방향)
    A, B = map(int, input().split()) # A To B
    graph[A].append(B)
    graph[B].append(A)
count = 0
DFS(1)
print(count-1) # 영향받는 컴퓨터의 수