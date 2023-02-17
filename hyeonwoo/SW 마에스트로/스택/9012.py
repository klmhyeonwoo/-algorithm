import sys

num = int(sys.stdin.readline())
temp = ''

for i in range(num):
    statement = sys.stdin.readline().rstrip()
    temp = statement
    while True:
        statement = statement.replace("()", "", 1)
        if (temp == statement):
            break
        else:
            temp = statement
    if (len(statement) >= 1):
        print("NO")
    else:
        print("YES")


# statement = sys.stdin.readline().rstrip()
# statement = statement.replace("()", "", 1)
# statement = statement.replace("()", "", 1)
# print(statement.replace("()", "", 1))
