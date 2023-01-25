# 2019 KAKAO BLIND RECRUITMENT 오픈채팅방

def solution(record):
    enterDict = {}
    leaveDict = []
    answer = []

    for item in record:
        data = item.split(' ')
        if (data[0] == 'Enter'):
            enterDict[data[1]] = data[2]
        elif (data[0] == 'Leave'):
            leaveDict.append(data[1])
        elif (data[0] == 'Change'):
            if (data[1] in enterDict):
                enterDict[data[1]] = data[2]

    for item in record:
        data = item.split(' ')
        if (data[0] == 'Enter'):
            if (data[1] in enterDict):
                answer.append(f'{enterDict[data[1]]}님이 들어왔습니다.')
        elif (data[0] == 'Leave'):
            if (data[1] in enterDict):
                answer.append(f'{enterDict[data[1]]}님이 나갔습니다.')

    return answer
