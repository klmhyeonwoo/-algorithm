#n = int(input())
n = int(input())
# 1234 / 1 % 10,  12 % 10, 123 % 10, 1234 % 10 
# 1234 % 
answer = 0

for i in range(1, n):
    sum = 0
    c = i
    divide = 1
    count = -1 

    while (c != 0): # 자리수 탐색
        c = c // 10
        count += 1

    divide = 10 ** count


    while divide > 0:
        a =  i // divide % 10
        sum += a
        divide = divide // 10

    if sum + i == n:
        answer = i
        break
        
print(answer)

