from collections import Counter

# 할인 행사


def solution(want, number, discount):

    lst = {}
    answer = 0

    for i in range(0, len(want)):
        lst[want[i]] = number[i]

    # print("hmm", Counter(lst))

    for i in range(0, len(discount)):
        if (discount[i] in want):
            if (len(discount[i:sum(number)+i]) == sum(number)):
                # print(len(discount[i:10+i]))
                if (lst == Counter(discount[i:sum(number)+i])):
                    answer += 1
                    # break
                    # print(Counter(discount[i:10+i]))
                    # print("일치!")

    return answer

    # 회원을 대상으로 매일 한 가지 제품을 할인하는 행사
    # 할인하는 제품은 하루에 하나씩만 구매 가능
    # 자신이 원하는 제품과, 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입

    # 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개
    # 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나

    # ["banana", "apple", "rice", "pork", "pot"]
    # [3, 2, 2, 2, 1]
    # ["chicken", "apple", "apple", "banana", "rice", "apple-", "pork", "banana-", "pork", "rice", "pot", "banana", "apple", "banana"]

    # discount 리스트로 순회하면서, 해당 아이템이 want에 있으면, discount를 10의 크기로 자르고 count 하면서 아니다 싶음 다음으로?
