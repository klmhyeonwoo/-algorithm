const fs = require('fs');
const [n, m, v, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

console.log(n, m, v, arr);

const N = parseInt(n); // 정점의 개수
const M = parseInt(m); // 간선의 개수
const V = parseInt(v); // 탐색을 시작할 정점의 번호

const listOfDFS = [];

const DFS = (node, v, visited) => {
    visited[v] = true;
    listOfDFS.push(v);
    for (let i of node[v]) {
        if (visited[i] === false) {
            DFS(node, i, visited);
        }
    }
}

const ChangeNumOfList = list => list.map(Number);
const Sort = (list) => {
    list.sort((a, b) => {
        if (a > b) {
            return 1;
        }
        if (a < b) {
            return -1;
        }
        if (a === b) {
            return 0;
        }
    })
    return list;
}
let lst = ChangeNumOfList(arr);

let visited = [];
let node = [];
for (let i=0; i<=N; i++) {
    visited.push(false); // 정점 + 1 만큼의 false 값을 만들어준다.
    node.push([]); // 정점 + 1 만큼의 [] 빈 배열을 만들어준다.
}

console.log(lst);

for (let k=0; k<lst.length; k+=2) {
    let a = lst[k];
    let b = lst[k+1];
    node[a].push(b);
    node[b].push(a);
}

for (let z=0; z<=N; z++) {
    Sort(node[z]);
}

DFS(node, V, visited);
console.log(...listOfDFS);