import re


def solution(str):

    # 1단계
    str = str.lower()

    # 2단계 (알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거)
    temp2 = ''
    for i in str:
        if ("0" <= i <= "9"):  # 숫자 일 경우를 넣어줘요
            temp2 += i
        elif ("a" <= i <= "z"):  # 알파벳 소문자일 경우를 넣어줘요
            temp2 += i
        elif (i == "-"):  # - 일 경우를 넣어줘요
            temp2 += i
        elif (i == '_'):  # _ 일 경우를 넣어줘요
            temp2 += i
        elif (i == '.'):  # . 일 경우를 넣어줘요
            temp2 += i

    # 3단계
    cnt = 0
    temp3 = ''
    for i in list(temp2):
        if (i == "."):
            cnt += 1
        else:
            if (cnt >= 1):
                temp3 += '.'
                temp3 += i
                cnt = 0
            else:
                temp3 += i

    print("temp3 :", temp3)
    # 4단계
    temp4 = ''
    if (temp3):
        if (temp3[0] == "."):  # str의 첫번째 글자가
            temp3 = temp3.replace(".", "", 1)

        if (temp3[-1] == "."):  # str의 마지막 글자가 . 일 경우에는 제거를 해줘요
            temp3 = temp3[:len(temp3)-1]

        temp4 = temp3

    print("temp4 :", temp4)

    # 5단계는 필요가 있넹
    if (temp4 == ""):
        temp4 = temp4.replace("", 'a')

    # 6단계
    if (len(temp4) >= 16):
        temp4 = temp4[:15]
        if (temp4[len(temp4)-1] == "."):
            temp4 = temp4[:len(temp4)-1]

    # 7단계
    if (len(temp4) <= 2):
        while (len(temp4) <= 2):
            temp4 = temp4 + temp4[len(temp4)-1]

    return temp4
