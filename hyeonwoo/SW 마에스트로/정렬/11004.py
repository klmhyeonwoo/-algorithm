import sys

N, K = map(int, sys.stdin.readline().split())
lst = []

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

print(lst[K-1])
