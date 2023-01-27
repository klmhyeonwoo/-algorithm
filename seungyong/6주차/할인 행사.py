import copy
def solution(want, number, discount):
    #회원가입을 하면 10일동안 하루에 한가지 할인
    #제품은 하루에 하나씩
    answer = 0
    w = []
    for i in range(len(want)): # 아이템의 개수대로 리스트에 추가
        for j in range(number[i]):
            w.append(want[i])
    

    for start in range(0,len(discount)): # 회원가입 날짜
        item = w.copy()
        count = 0 # 혜택 기간
        for index in range(start, len(discount)): # 회원가입 후 10일
            count += 1
            if discount[index] in item: # 10일동안 할인 품목 리스트에서 지우기
                item.remove(discount[index])
            if count == 10:
                break
        if item == []: # 리스트가 비었다면 모두 다 구매한 경우
            answer += 1
        
    
    return answer