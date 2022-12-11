import sys

result = []


def DFS(node, v, visited):
    global result
    visited[v] = True
    result.append(v)
    for i in node[v]:
        if (visited[i] == False):
            DFS(node, i, visited)


computer = int(sys.stdin.readline().rstrip())
nodeNum = int(sys.stdin.readline().rstrip())

visited = []

node = [[] for _ in range(computer + 1)]

for i in range(computer+1):
    visited.append(False)

for i in range(nodeNum):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    node[x].append(y)
    node[y].append(x)
# print(node)

for k in range(computer+1):
    node[k].sort()

DFS(node, 1, visited)

count = 0

# print(result)

for i in result:
    if (i != 1):
        count += 1

print(count)
