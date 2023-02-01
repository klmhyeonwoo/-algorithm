from itertools import product


def solution(users, emoticons):

    MAX_SUB = 0
    MAX_PRICE = 0

    # 중복조합을 통해 할인율의 모든 경우의 수를 섞어줘요
    percentList = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    # print(list(combinations_with_replacement([10,20,30,40], len(emoticons))))

    print(f'n명의 구매 기준 : {users}')
    print(f'm개의 정가를 담은 1차원 배열 : {emoticons}')

    for percent in percentList:  # 할인율을 담은 리스트를 돌려줍니다.
        SUB = 0
        TOTAL = 0
        for user in users:  # 사람 돌리는 로직 (한 명씩 차례로)
            PRICE = 0
            for i in range(0, len(emoticons)):
                # 중복조합을 통해 퍼센트를 섞어주었고, 해당 가격의 순서와 매칭시켜주면서 계산을 해주는 로직이에요
                if (user[0] <= percent[i]):  # 할인율에서 먼저 컷 해줍니다.
                    # print(f'할인율 : {z}, 유저의 구매 할인율 : {users[k][0]}')
                    PRICE += emoticons[i] - (emoticons[i] * (percent[i] / 100))
            if (PRICE >= user[1]):  # 사용자가 가지고 있는 가격보다 price 값이 크다면 구독자로 변경
                SUB += 1
            else:
                TOTAL += PRICE  # 넘지 않는다면 TOTAL 값에 저장을 해요

        if (MAX_SUB < SUB):  # 한 유저의 반복이 끝나고, 구독자의 수가 최대 구독자 수 보다 많다면, 기존의 구독자 수와 가격을 변경시켜줘요
            MAX_SUB = SUB
            MAX_PRICE = TOTAL

        elif (MAX_SUB == SUB):  # 최대 구독자 수와 구독자 수가 비슷하다면, 서로 가격이 높은 것을 최대 가격으로 설정해줘요
            if (MAX_PRICE < TOTAL):
                MAX_PRICE = TOTAL

    return [MAX_SUB, int(MAX_PRICE)]

    # 10%부터 돌리면서 40%까지
    # n명의 구매기준 `users`
    # m개의 정가를 담은 1차원 배열 `emoticons`

    # 이모티콘 플러스 서비스 가입자를 최대한 늘릴 것 (우선 목표)
    # 이모티콘 판매액을 최대한 늘리는 것 (서브 목표)

    # N명에게 M개를 할인하여 판매
    # 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됨

    # 사용자들은 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입을 한다.
    # 단 사용자는 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매하지만,
    # 하지만, 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 취소하고 이모티콘 플러스 서비스 가입

    # 자신에게 부여된 퍼센트의 할인율에 이상 할인하는 이모티콘을 모두 구매
    # 하지만, 이모티콘 구매 비용이 자신이 가진 가격을 초과하면 그냥 이모티콘 플러스 서비스에 가입

    # 4900 + 5400 = 10300
