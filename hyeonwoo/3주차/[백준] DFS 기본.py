import sys
from collections import deque

# 함수를 적는 칸이에요 👏🏻


def DFS(node, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in node[v]:
        if (visited[i] == False):
            DFS(node, i, visited)

# def DFS(graph, v, visited):
#     visited[v] = True
#     print(v, end = " ")
#     for i in node[v]:
#         if (visited[i] == False):
#             visited[i] = True
#             DFS(graph, v, visited)

# def BFS(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while(queue):
#         v = queue.popleft()
#         print(v)
#         for i in node[v]:
#             if (visited[i] == False):
#                 queue.append(i)
#                 visited = True


def BFS(node, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        # print("v", v)
        print(v, end=" ")
        for i in node[v]:
            if (visited[i] == False):
                queue.append(i)
                visited[i] = True

# 함수가 끝나는 칸이에요 👏🏻


N, M, V = map(int, sys.stdin.readline().rstrip().split())

visited = []

node = [[] for _ in range(N+1)]
for i in range(N+1):
    visited.append(False)

# print(visited)

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].append(b)
    node[b].append(a)
# print(node)

for k in range(N+1):
    node[k].sort()
    # print(node[k])

DFS(node, V, visited)
print('')

# BFS를 실행시켜주기 위해서, 모든 방문기록을 Falsee로 만들어줍니다.
for i in range(N+1):
    visited[i] = False

BFS(node, V, visited)
