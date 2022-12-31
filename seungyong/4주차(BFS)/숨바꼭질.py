from collections import deque

N, M = map(int, input().split())
visited = [False for i in range(100001)]

cnt = 0
queue = deque([(N, cnt)])
visited[N] = True
while(queue): 
  x, cnt = queue.popleft()
  if x == M:
    break
  if x + 1 < 100001:
    if visited[x + 1] == False:
      queue.append((x + 1, cnt + 1))
      visited[x + 1] = True
  if x - 1 >= 0:
    if visited[x - 1] == False:
      queue.append((x - 1, cnt + 1))
      visited[x - 1] = True
  if x * 2 < 100001:
    if visited[x * 2] == False:
      queue.append((x * 2, cnt + 1))
      visited[x * 2] = True

print(cnt)
