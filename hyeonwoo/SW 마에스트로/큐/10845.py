import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if (command[0] == "push"):
        queue.append(command[1])
    elif (command[0] == "pop"):
        if (queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif (command[0] == "size"):
        print(len(queue))
    elif (command[0] == "empty"):
        if (queue):
            print(0)
        else:
            print(1)
    elif (command[0] == "front"):
        if (queue):
            print(queue[0])
        else:
            print(-1)
    elif (command[0] == "back"):
        if (queue):
            print(queue[-1])
        else:
            print(-1)
