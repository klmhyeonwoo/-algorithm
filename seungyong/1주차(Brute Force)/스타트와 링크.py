from itertools import combinations
 
N = int(input())
person = [i for i in range(N)]

teamStat = []
for row in range(N):
    lst = list(map(int,input().split()))
    teamStat.append(lst)
#print(teamStat)

team = list(combinations(person,N//2))
min = 1000000000000
for start in team: # start팀이 될 수 있는 조합 N개중 2개 선택
    link = []
    for n in range(N):
        if n not in start: 
            link.append(n)
    #print(start)
    #print(link)

    combiStart = list(combinations(start,2))
    sumStart = 0
    for i, j in combiStart:
        sumStart += teamStat[i][j]
        sumStart += teamStat[j][i]

    combiLink = list(combinations(link,2))
    sumLink = 0
    for i, j in combiLink:
        sumLink += teamStat[i][j]
        sumLink += teamStat[j][i]
    
    s = abs(sumLink - sumStart)
    if min > s:
        min = s
print(min)
