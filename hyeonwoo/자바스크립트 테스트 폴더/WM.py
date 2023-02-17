def find(a):

    n = "a"

    answer = False
    cnt = len(a)
    result = [False]*(len(a))
    print(result)

    for j in range(len(a)):
        sum_a = 0
        for i in n:
            # print(i)
            if i == "a":
                sum_a += 1
            print(i)
        print()
        n = "b"*sum_a+n+"b"*sum_a
        # print(n)
        # print(sum_a)

        for k in range(len(a)):

            if a[k] == "a"+n or n+"a" == a[k] or a[k] == "aa"+n or n+"aa" == a[k]:
                answer = True
                result[k] = "true"

        n = "a"+n+"a"

    return result


print(find(["abab", "bbaa", "bababa", "bbbabababbbaa"]))
