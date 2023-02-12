import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if (command[0] == "push_front"):
        stack.insert(0, command[1])
    elif (command[0] == "push_back"):
        stack.append(command[1])
    elif (command[0] == "pop_front"):
        if (stack):
            stack.pop(0)
        else:
            print(-1)
    elif (command[0] == "pop_back"):
        if (stack):
            stack.pop()
        else:
            print(-1)
    elif (command[0] == "size"):
        print(len(stack))
    elif (command[0] == "empty"):
        if (stack):
            print(0)
        else:
            print(1)
    elif (command[0] == "front"):
        if (stack):
            print(stack[0])
        else:
            print(-1)
    elif (command[0] == "back"):
        if (stack):
            print(stack[-1])
        else:
            print(-1)
