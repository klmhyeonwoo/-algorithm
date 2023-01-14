from collections import deque

def solution(board, moves):
    board.reverse()
    queue = [deque([]) for i in range (len(board))]
    bucket = []
    temp = []
    count = 0
    
    # 세로로 나열해주었음
    for i in range (0, len(queue)):
        for k in range (0, len(queue)):
            if (board[k][i] != 0):
                queue[i].append(board[k][i])
            
    # 테스트
    # print(queue)
    
    for i in moves:
        # print(f'{i} : {queue[i-1].popleft()}')
        if (queue[i-1]):
            bucket.append(queue[i-1].pop())
    # print(bucket)
    
    for i in bucket:
        if (temp):
            if (temp[-1] == i):
                temp.pop()
                count += 2
                continue
        temp.append(i)
    
    return count
