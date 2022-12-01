def permutation(level):
    global M
    if len(lst) == M: # 중단조건 M개 고르면 끝
        for k in lst:
            print(k,end=' ')
        print()
        return

    for i in range(1, N + 1):
            lst.append(i)
            permutation(level + 1)
            lst.pop()
 
N, M = map(int, input().split())
lst = []
visited = [False for _ in range(0,N+1)] # 0 ~ N

permutation(1)

"""
4C2 
permutation(1) 호출 
for 1 in range(1 ~ 4)
	permutation(2)호출 [1]
	for 2 in range(2 ~ 4) 
		permutaion(3)호출 [1,2]
		for 3 in range( 3 ~ 4)
			permutation(4)호출 [1,2,3] -> !중단조건! -> 1 2 3 출력
		for 4 in range( 4 ~ 4)
			permutation(5)호출 [1,2,4] -> !중단조건! -> 1 2 4 출력
      ->for 3 in range(3 ~ N)
		permutation(4)호출 [1,3]
		for 4 in range(4 ~ 4)
			permutation(5)호출 [1,3,4] -> !중단조건! -> 1 3 4 출력
      ->for 4 in range(4 ~ N)
		permutation(5)호출 [1,4]
		for 5 in range(5 ~ 4) -> X

for 2 in range(2 ~ 4)
	permutation(3)호출 [2]
	for 3 in range(3 ~ 4) 
		permutaion(4)호출 [2,3]
		for 4 in range(4 ~ 4)
			permutation(5)호출 [2,3,4] -> !중단조건! -> 2 3 4 출력
      ->for 4 in range(3 ~ 4)
		permutation(5)호출 [2,4]
		for 5 in range(5 ~ 4) X

for 3 in range(3 ~ 4)
	permutation(4)호출 [3]
	for 4 in range(4 ~ 4) 
		permutaion(5)호출 [3,4]
		for 5 in range(5 ~ 4) X

"""