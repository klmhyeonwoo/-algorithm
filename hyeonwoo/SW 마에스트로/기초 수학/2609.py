import sys

num1, num2 = map(int, sys.stdin.readline().split())

minNum = min(num1, num2)
minNum2 = min(num1, num2)
mul = 2

while True:
    if (num1 % minNum == 0 and num2 % minNum == 0):
        break
    else:
        minNum -= 1

while True:
    if (minNum2 % num1 == 0 and minNum2 % num2 == 0):
        break
    else:
        minNum2 += minNum2

print(minNum)
print(minNum2)
