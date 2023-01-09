from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    num = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        # print(f'queue : {queue}')
        a, b = queue.popleft()
        # print(f'흠,, {a, b}')
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (nx < 0 or nx >= num or ny < 0 or ny >= num):
                continue
            if (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


graph = []
num = int(sys.stdin.readline())

for i in range(num):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# graph에 잘 들어갔는지 확인을 해주십시다!
# print(graph)

count = []
for x in range(num):
    for y in range(num):
        if (graph[x][y] == 1):
            count.append(bfs(graph, x, y))

# 셈수 오름차순으로 정렬
count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])
