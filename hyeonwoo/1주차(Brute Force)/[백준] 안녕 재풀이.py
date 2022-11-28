from itertools import combinations
import sys

N = int(sys.stdin.readline())

newLife = 100
newJoy = 0
minusLife = list(map(int, sys.stdin.readline().split()))
fillJoy = list(map(int, sys.stdin.readline().split()))

newArray = []
for x, y in zip(minusLife, fillJoy):
    newArray.append([x,y])

for z in range (1, N+1):
    test = list(combinations(newArray, z))
    if (len(test) == 0):
        break

    for i in test:
        life_temp = 0
        joy_temp = 0
        for k in i:
            life_temp -= k[0]
            joy_temp += k[1]
            if (abs(life_temp) < 100 and joy_temp > newJoy):
                newLife = life_temp
                newJoy = joy_temp

print(newJoy)


