const fs = require('fs');
const [n, m, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

let dfsOfList = [];
let count = 0;

const DFS = (nodes, v, visited) => {
    visited[v] = true;
    dfsOfList.push(v);
    for (let i of nodes[v]) {
        if (visited[i] === false) {
            DFS(nodes, i, visited);
        }
    }
}

const ChangeNumList = (arr) => arr.map(Number);
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
const lst = ChangeNumList(arr);
const N = parseInt(n);
const M = parseInt(m);
const visited = [];
const nodes = [];

for (let i=0; i<=N; i++) {
    visited.push(false);
    nodes.push([]);
} // 정점 + 1의 개수만큼 방문 기록을 만들어주고, 요소들을 담을 노드를 만들어줍니다.

for (let k=0; k<lst.length; k+=2) {
    const a = lst[k];
    const b = lst[k+1];

    nodes[a].push(b);
    nodes[b].push(a);
}

for (let z=0; z<=N; z++) {
    Sort(nodes[z]);
}


for (let t=1; t<=N; t++) {
    if (visited[t] === false) {
        count += 1;
        DFS(nodes, t, visited);
    }
}

console.log(count)
