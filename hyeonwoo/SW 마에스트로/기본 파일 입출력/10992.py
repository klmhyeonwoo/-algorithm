import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    for a in range(N, i, -1):
        print("-", end="")
    for b in range(0, i*2-1):
        if (i == N):
            print("*", end="")
        elif (1 <= b and b < i*2-2):
            print(" ", end="")
        else:
            print("*", end="")
    print()

'''
   * # 
  * *
 *   *
*******
'''
