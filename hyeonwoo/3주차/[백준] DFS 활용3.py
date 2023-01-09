import sys
sys.setrecursionlimit(10000)

# DFS 정의
def dfs(x, y):
    # 상,하, 좌,우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                # 방문했다는 표시 -1
                graph[ny][nx] = -1
                dfs(nx, ny)


# 테스트 케이스
t = int(input())

for i in range(t):
    # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    result = 0

    # 배추 위치에 1 표시
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    # DFS를 활용해서 배추 그룹 수 세기
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                result += 1

    print(result)
# print(graph)
