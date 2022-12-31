from collections import deque
dy = [-1, -1, -1, 0, 1, 1,  1,  0]
dx = [-1,  0,  1, 1, 1, 0, -1, -1]

def BFS(start):
  queue = deque([start])

  
  while(queue):
    x, y  = queue.popleft()

    for i in range(8):
      nextY = y + dy[i]
      nextX = x + dx[i]
      if 0 <= nextX < w and 0 <= nextY < h and m[nextY][nextX] == 1:
        queue.append((nextX, nextY))
        m[nextY][nextX] = 0



while(True):
  w, h = map(int,input().split())
  if w == 0 and h == 0:
    break

  m = []
  for i in range(h):
    lst = list(map(int, input().split()))
    m.append(lst)

  island = 0 # 섬의 수
  for row in range(h):
    for col in range(w):
      if m[row][col] == 1:
        island += 1
        m[row][col] = 0
        BFS((col, row))
        
  print(island)



