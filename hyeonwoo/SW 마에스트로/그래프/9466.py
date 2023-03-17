# 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    if visited[student[x]]:
        if student[x] in cycle:
            result += cycle[cycle.index(student[x]):]
        return
    else:
        dfs(student[x])


T = int(input())
for _ in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    student.insert(0, 0)
    visited = [False] * (N+1)
    result = []

    print(student)

    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N-len(result))
