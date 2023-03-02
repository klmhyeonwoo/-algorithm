const fs = require('fs');
const [n, k, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

let cnt = 0;
let minimize = 999;

let N = parseInt(n) // 경우의 수
let K = parseInt(k) // 돈

arr.reverse()

for (let i of arr) {
    i = parseInt(i)
    if (K >= i && Math.floor(K / i) != 0) {
        minimize = Math.min(minimize, Math.round(K / i));
        cnt += Math.floor(K / i);
        // console.log(i, cnt, K, (K / i).toFixed())
        K = Math.round(K % i);
    }
}

console.log(cnt)