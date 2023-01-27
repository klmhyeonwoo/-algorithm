########################### 실행 코드 #####################################
graph = []
def rotate(x1, y1, x2, y2):
    cX = x1 # currnetX
    cY = y1 # currentY
    cV = graph[cY][cX]  # currentValue
    values = [] #minValue
    while(True):
        values.append(cV)
        nY = -1; nX = -1 # nextY, nextX
        if x1 <= cX < x2 and cY == y1: # 상단
            nY = y1
            nX = cX + 1
        elif cX == x2 and y1 <= cY < y2: #우측
            nY = cY + 1
            nX = x2
        elif x1 < cX <= x2 and cY == y2: #하단
            nY = y2
            nX = cX - 1
        elif cX == x1 and y1 < cY <= y2: #좌측
            nY = cY - 1
            nX = x1
        
        
        
        
        temp = graph[nY][nX]
        graph[nY][nX] = cV
        cV = temp
        cY = nY
        cX = nX
        if nY == y1 and nX == x1:
            break
            
    return min(values)

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


answer = []
for row in range(rows): # 0 1 2 3 4 5
  lst = []
  for col in range(1, columns + 1): # 1 2 3 4 5 6
    lst.append(row * columns + col)
  graph.append(lst)


for querie in queries:
  y1,x1,y2,x2 = querie
  print(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    

###################  programmers code  ##############################

graph = []
def rotate(x1, y1, x2, y2):
    cX = x1 # currnetX
    cY = y1 # currentY
    cV = graph[cY][cX]  # currentValue
    values = [] #minValue
    while(True):
        values.append(cV)
        nY = -1; nX = -1 # nextY, nextX
        if x1 <= cX < x2 and cY == y1: # 상단
            nY = y1
            nX = cX + 1
        elif cX == x2 and y1 <= cY < y2: #우측
            nY = cY + 1
            nX = x2
        elif x1 < cX <= x2 and cY == y2: #하단
            nY = y2
            nX = cX - 1
        elif cX == x1 and y1 < cY <= y2: #좌측
            nY = cY - 1
            nX = x1
        
        
        
        
        temp = graph[nY][nX]
        graph[nY][nX] = cV
        cV = temp
        cY = nY
        cX = nX
        if nY == y1 and nX == x1:
            break
            
    return min(values)

def solution(rows, columns, queries):

    answer = []
    for row in range(rows): # 0 1 2 3 4 5
        lst = []
        for col in range(1, columns + 1): # 1 2 3 4 5 6
            lst.append(row * columns + col)
        graph.append(lst)


    for querie in queries:
        y1,x1,y2,x2 = querie
        answer.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    
    return answer