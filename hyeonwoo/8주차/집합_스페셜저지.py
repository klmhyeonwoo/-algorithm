import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(0, N+1)]
# print(parent)


def find_parent(x):
    if (parent[x] != x):
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    # print("a :", a, "b :", b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    # print(parent)


for _ in range(M):
    command, a, b = map(int, sys.stdin.readline().rstrip().split())

    if (command == 0):
        union_parent(a, b)

    if (command == 1):
        if (find_parent(a) == find_parent(b)):
            print("YES")
        else:
            print("NO")
