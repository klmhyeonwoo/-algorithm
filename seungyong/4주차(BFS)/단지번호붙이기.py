from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def BFS(start):
  global count
  queue = deque([start])

  
  while(queue):
    x, y  = queue.popleft()

    for i in range(4):
      nextY = y + dy[i]
      nextX = x + dx[i]
      if 0 <= nextX < N and 0 <= nextY < N and m[nextY][nextX] == 1:
        queue.append((nextX, nextY))
        m[nextY][nextX] = 0
        count += 1



N = int(input())

m = []
for i in range(N):
  str = input()
  lst = []
  for c in str:
    lst.append(int(c))
  m.append(lst)

house = [] # 단지 내 집의 수 배열
cnt = 0 # 아파트 단지 수
for row in range(N):
  for col in range(N):
    if m[row][col] == 1:
      count = 0 # 단지 내 집의 수
      cnt += 1
      m[row][col] = 0
      count += 1
      BFS((col, row))
      house.append(count)

print(cnt)
house.sort()
for h in house:
  print(h)



