import sys

info = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
temp = 0

month, day = map(int, sys.stdin.readline().split())

for i in range(1, month):
    day += info[i]

print(date[day % 7])
