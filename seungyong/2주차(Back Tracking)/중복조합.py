def combination(level):
    global M
    if len(lst) == M: # 중단조건 M개 고르면 끝
        for k in lst:
            print(k,end=' ')
        print()
        return

    for i in range(level, N + 1):
            lst.append(i)
            combination(i)
            lst.pop()
			
 
N, M = map(int, input().split())
lst = []
visited = [False for _ in range(0,N+1)] # 0 ~ N

combination(1)

"""
4개중 3개 중복조합
1 -> 123(1) -> 123(1,2,3)
111
112
113
1 -> 123(2) -> 23(2,3)
122
123

1 -> 123(3) -> 3(3)
133

2 -> 23(2) -> 23(2,3)
2 2 2
2 2 3

2 -> 23(3) -> 3(3)
2 3 3

3 -> 3(3) -> 3(3)   
333

"""