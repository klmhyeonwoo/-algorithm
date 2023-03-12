
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
test_num = int(input())

isValied = True


def dfs(start):
    global isValied
    visited[start] = True
    for i in adjacent[start]:
        if not visited[i]:
            team[i] = (team[start]+1) % 2
            dfs(i)
        elif team[start] == team[i]:
            isValied = False


for _ in range(test_num):
    isValied = True
    v, e = map(int, input().split())
    visited = [False] * (v+1)
    adjacent = [[]for _ in range(v+1)]
    team = [0] * (v+1)  # T집합 또는 F집합
    for _ in range(e):
        p, q = map(int, input().split())
        adjacent[p].append(q)
        adjacent[q].append(p)
    for i in range(1, v+1):
        if isValied:
            dfs(i)
        else:
            break
    if isValied:
        print("YES")
    else:
        print("NO")
