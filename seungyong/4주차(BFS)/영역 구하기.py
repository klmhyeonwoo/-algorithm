from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]

M, N, K = map(int, input().split())
m = [[False for i in range(N)] for j in range(M)]

for k in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for y in range((M-1) - y2 + 1, (M - 1) - y1 + 1):# 2 ~  
    for x in range(x1, x2):
      m[y][x] = True

#for a in m:
#  print(a)
count = 0
area = []
for row in range(M):
  for col in range(N):
    if m[row][col] == False:
      count += 1
      
      queue = deque([(row ,col)])
      m[row][col] = True
      a = 1
      while(queue):
        r, c = queue.popleft()

        for i in range(4):
          y = r + dy[i]
          x = c + dx[i]
          if 0 <= y < M and 0 <= x < N:
            if m[y][x] == False:
              queue.append((y,x))
              a += 1
              m[y][x] = True
      area.append(a)
print(count)
area = sorted(area)
for i in area:
  print(i,end=' ')
