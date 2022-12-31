import sys
sys.setrecursionlimit(2500) # 백준 채점시 재귀 1000회까지라서 제한 설정

dx = [0,1,0,-1] # 위 오 아 왼
dy = [-1,0,1,0]

def printMap(m):
    for m_ in m:
        print(m_)

def DFS(row, col):

    m[row][col] = 0 # 방문처리
    
    for i in range(4):   # 해당 좌표 기준 위 오른쪽 아래 왼쪽 좌표
        y = row + dy[i]  
        x = col + dx[i] 
        if 0 <= y and y < N and 0 <= x and x < M and m[y][x] == 1: # 이동할 곳이 범위 내 + 배추라면
            DFS(y, x)


T = int(input())
for t in range(T):
    M, N, L = map(int, input().split())

    m = [[0 for col in range(M)] for row in range(N)]
    for i in range(L):
        col, row  = map(int, input().split())
        m[row][col] = 1
    count = 0
    for row in range(N):
        for col in range(M):
            if m[row][col] == 1: # 전체 맵을 돌다가 배추를 만난다면
                count += 1
                DFS(row, col) # DFS 때마다 배추영역이 사라짐! 
                #printMap(m)
                #print()

    print(count)
