const fs = require('fs');
const [n, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

function Sort(list) {
    list.sort((a,b) => {
        if (a > b) {
            return 1;
        }
        if (a < b) {
            return -1;
        }
        if (a === 0) {
            return 0;
        }
    })
    return lst;
}

function ReverseSort(list) {
    Sort(list);
    list.reverse()
    return list;
}

const N = parseInt(n); // 경우의 수 
const changeNum = arr => arr.map(Number); // 문자열로 들어온 JS 배열을 숫자로 바꿔주는 함수
const lst = changeNum(arr);

let plus = [];
let minus = [];
let result = 0;

for (let item of lst) {
    if (item > 1) {
        plus.push(item);
    } else if (item <= 0) {
        minus.push(item);
    } else {
        result += item;
    }
}

ReverseSort(plus); // 양수의 경우 reverse를 통해 큰 수부터 곱해야 가장 큰 값이 나온다.
Sort(minus) // 음수의 경우 가장 작은 마이너스 값을 곱했을 때 가장 큰 값이 나온다.

console.log(plus, minus);

// 양수 묶기
for (let i=0; i<plus.length; i+=2) {
    if (i+1 >= plus.length) {
        result += plus[i];
    } else {
        result += (plus[i] * plus[i + 1]);
    }
}

// 음수 묶기
for (let i=0; i<minus.length; i+=2) {
    if (i+1 >= minus.length) {
        result += minus[i]
    } else {
        result += (minus[i] * minus[i + 1]);
    }
}

console.log(result)
