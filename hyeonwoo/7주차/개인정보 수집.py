from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):

    today = datetime.strptime(today, '%Y.%m.%d')
    print("today :", today)

    answer = []
    newDict = {}

    # 보기 쉽게 딕셔너리로 만들어줍니다!
    for items in terms:
        items = items.split(" ")
        newDict[items[0]] = items[1]

    for i in range(len(privacies)):
        item = privacies[i].split(" ")
        newTime = datetime.strptime(item[0], '%Y.%m.%d')
        scaledTime = newTime + relativedelta(months=int(newDict[item[1]]))

        print(scaledTime)

        if (scaledTime <= today):
            answer.append(i + 1)

    print(answer)
    print(newDict)

    return answer


# 1~n 번으로 분류되는 개인정보 n개
# 각 약관마다 개인정보 보관 유효기간이 정해져있음
# 나는, 각 개인정보가 어떤 약관으로 수집됐는지 알고 있음
# 수집된 개인정보는 유효기간 전까지만 보관 가능하고, 유효기간이 지났다면 반드시 파기

# A - 12달, 2021년 1월 5일에 수집된 개인정보 2022년 1월 4일까지 보관 가능하며
# 12달 -> 1년 플러스해주고 1일 마이너스?
