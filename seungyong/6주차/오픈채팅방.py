def solution(records):
    result = []
    answer = []
    nameById = {}
    for record in records:
        r = record.split(" ")
        id = r[1] 
        if r[0] == 'Enter':
            nameById[id] = r[2] # 닉네임 등록
            action = "님이 들어왔습니다."
            result.append([id, action])
        elif r[0] == "Leave":
            action = "님이 나갔습니다."
            result.append([id, action])
        else: # 닉네임 변경
            nameById[r[1]] = r[2]
    
    for r in result:  # result['uid1234',님이 들어왔습니다]
        answer.append(nameById[r[0]] + r[1])
    return answer

