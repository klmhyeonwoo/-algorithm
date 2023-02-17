import sys

num = int(sys.stdin.readline())
stack = []

for i in range(num):
    command = sys.stdin.readline().rstrip().split()

    if (command[0] == "push"):  # 정수 X를 스택에 넣는 연산이다.
        stack.append(command[1])
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력하고 만약 스택에 들어있는 정수가 없는 경우 -1을 출력한다.
    elif (command[0] == "pop"):
        if (stack):
            print(stack.pop())
        else:
            print(-1)
    elif (command[0] == "size"):
        print(len(stack))
    elif (command[0] == "empty"):
        if (stack):
            print(0)
        else:
            print(1)
    elif (command[0] == "top"):
        if (stack):
            print(stack[-1])
        else:
            print(-1)
