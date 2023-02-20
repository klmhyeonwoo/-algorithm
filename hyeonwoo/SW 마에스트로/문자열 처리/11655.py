import sys

word = sys.stdin.readline().rstrip()
lst = []

for i in word:
    if (i == " "):
        lst.append(" ")
    elif (i >= "0" and i <= "9"):
        lst.append(i)
    else:
        if (i.islower()):
            lst.append(chr(97+(ord(i)+13-97) % 26))
        elif (i.isupper()):
            lst.append(chr(65+(ord(i)+13-65) % 26))

print(''.join(lst))
