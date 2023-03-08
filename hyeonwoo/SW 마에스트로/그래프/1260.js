const fs = require('fs');
const [n, m, v, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const ChangeNumList = (list) => list.map(Number);
const sort = (list) => {
    list.sort((a, b) => {
        if (a > b) {
            return 1;
        } else if (a < b) {
            return -1
        } else if (a === b) {
            return 0;
        }
    })

    return list;
}

// 문자열로 들어온 리스트 및 변수를 먼저 숫자로 바꿔줍니다.
let N = parseInt(n);
let M = parseInt(m);
let V = parseInt(v);
let lst = ChangeNumList(arr);
let visited = []
let node = []

// 방문 기록을 위해 N+1 만큼의 false 칸을 만들어줍니다.
for (let k=0; k<=N; k++) {
    visited.push(false);
}

// 각 칸 마다 담을 배열을 만들어줍니다.
for (let i=0; i<=M; i++) {
    node.push([]);
}

// 만들어준 node라는 변수에 숫자를 넣어줍니다.
for (let z=0; z<lst.length; z+= 2) {
    let a = lst[z];
    let b = lst[z+1];

    node[a].push(b);
    node[b].push(a);
}

for (let y=0; y<=N; y++) {
    sort(node[y]);
}

console.log(node)

// console.log(N, M, V, arr);


