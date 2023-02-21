import sys

while True:
    emptyCount = 0
    numCount = 0
    lowerCount = 0
    upperCount = 0
    word = sys.stdin.readline().rstrip('\n')

    if (not word):
        break

    for i in word:
        if (i.islower()):
            lowerCount += 1
        elif (i.isupper()):
            upperCount += 1
        elif (i == " "):
            emptyCount += 1
        elif ("0" <= i) and ("9" >= i):
            numCount += 1

    print(lowerCount, upperCount, numCount, emptyCount)
