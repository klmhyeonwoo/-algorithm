from itertools import combinations



N = int(input())
health = list(map(int, input().split()))
delight = list(map(int, input().split()))
maxDelight = 0

idxList = []
for i in range(N):
    idxList.append(i)

for n in range(1,N + 1):
    combi = list(combinations(idxList, n))

    for idxs in combi:
        sumDelight = 0
        sumHealth  = 0
        #print(idxs)
        for idx in idxs:
            sumDelight += delight[idx]
            sumHealth += health[idx]
        #print(sumDelight, sumHealth)
        if sumHealth >= 100:
            continue
        else:
            if sumDelight > maxDelight:
                maxDelight = sumDelight 
print(maxDelight)        

