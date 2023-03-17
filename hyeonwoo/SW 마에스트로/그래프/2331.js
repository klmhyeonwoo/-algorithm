const fs = require('fs');
const [a, n] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

let A = a;
const N = parseInt(n);
const lst = [parseInt(a)]; // 기본적으로 a는 들어가있습니다.
let index = 0;

while(1) {
    let num = 0;
    for (let i of A) {
        num += parseInt(i) ** N;
    }

    A = String(num);

    if (lst.includes(parseInt(A))) {
        index = num
        break;
    } else {
        lst.push(num);
    }
}

console.log(lst.slice(0,lst.indexOf(index)).length)