import sys

while (1):
    word = sys.stdin.readline().rstrip()
    if (word == ''):
        break
    else:
        print(word)


# OR

import sys

while (1):
    try:
        word = input()
        print(word)
    except EOFError:
        break
