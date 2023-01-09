import sys

result = []


def DFS(node, v, visited):
    global result
    visited[v] = True
    result.append(v)
    for i in node[v]:
        if (visited[i] == False):
            DFS(node, i, visited)


T = int(sys.stdin.readline().rstrip())

for i in range(T):
    width, height, num = map(int, sys.stdin.readline().rstrip().split())
    visited = []

    for i in range(width+1):
        visited.append(False)

    node = [[] for _ in range(width+1)]
    for i in range(num):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        node[x].append(y)
        # node[y].append(x)

    for k in range(width+1):
        node[k].sort()

    for i in range(height):
        DFS(node, i, visited)

print(node)
print(set(result))
