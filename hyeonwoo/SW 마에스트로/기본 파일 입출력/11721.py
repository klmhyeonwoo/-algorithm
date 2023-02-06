import sys

word = sys.stdin.readline().rstrip()

div = len(word) // 10
remain = len(word) % 10
temp = 0

for i in range(1, div + 1):
    print(word[temp*10:i*10])
    temp += 1

print(word[temp*10:temp*10+remain])
