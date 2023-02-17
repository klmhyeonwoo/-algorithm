function solution(a) {
    let result = [];
    for (let s of a) {
        let x = 0;
        let temp = s;
        while (temp[0] === 'a') {
            x++;
            temp = temp.slice(1);
        }
        let flag = true;
        while (temp.length > 0) {
            let count = 0;
            while (temp[count] === 'a') {
                count++;
            }
            if (count === 0) {
                flag = false;
                break;
            } else if (count === x) {
                temp = temp.slice(count);
                x = count * 2;
            } else {
                flag = false;
                break;
            }
            if (temp.length > 0 && temp[0] === 'a') {
                x++;
                temp = temp.slice(1);
            }
        }
        result.push(flag);
    }
    return result;
}

solution(["abab", "bbaa", "bababa", "bbbabababbbaa"])

// def find(lst):


//     n="a"

//     answer=False
//     cnt=len(lst)
//     result=[False](len(lst))

//     for j in range(len(lst)):
//         sum_a=0
//         for i in n:
//             if i=="a":
//                 sum_a+=1
//         n="b"sum_a+n+"b"*sum_a

//         for k in range(len(lst)):

//             if lst[k]=="a"+n or n+"a"==lst[k] or lst[k]=="aa"+n or n+"aa"==lst[k]:
//                 answer=True
//                 result[k]="true"

//         n="a"+n+"a"






//     return result