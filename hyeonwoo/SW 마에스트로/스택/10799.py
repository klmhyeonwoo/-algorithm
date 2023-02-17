import sys
import math

statement = sys.stdin.readline().rstrip()
answer = 0
stack = []

for i in range(len(statement)):
    # '('이 나올 경우 stack에 push
    if (statement[i] == '('):
        stack.append(statement[i])

    # '('이 아닐 경우 그 전 문자열이 '(' 일 경우 stack에서 1개를 pop하고 스택의 크기만큼 result에 더해준다.
    else:
        if (statement[i-1] == '('):
            stack.pop()
            answer += len(stack)

        # ')' 일 경우에는 막대기가 있는 것이므로 1개를 result에 증가시켜준다.
        else:
            stack.pop()
            answer += 1
print(answer)

# statement = sys.stdin.readline().rstrip()
# statement = statement.replace("()", "", 1)
# statement = statement.replace("()", "", 1)
# print(statement.replace("()", "", 1))
