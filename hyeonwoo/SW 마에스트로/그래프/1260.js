const fs = require('fs');
const [n, m, v, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const bfsOfList = [];
const dfsOfList = [];

const N = parseInt(n);
const M = parseInt(m);
const V = parseInt(v);

const DFS = (node, v, visited) => {
    visited[v] = true;
    dfsOfList.push(v);
    for (let i of node[v]) {
        if (visited[i] === false) {
            DFS(node, i, visited);
        }
    }
}

const BFS = (node, v, visited) => {
    const queue = [v];
    visited[v] = true;
    while (queue.length > 0) {
        let num = queue.shift();
        bfsOfList.push(num);
        for (let i of node[num]) {
            if (visited[i] === false) {
                queue.push(i);
                visited[i] = true;
            }
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
const node = [];
const visited = [];

for (let i=0; i<=N; i++) {
    node.push([]);
    visited.push(false);
}

for (let k=0; k<lst.length; k+=2) {
    let a = lst[k];
    let b = lst[k + 1];

    node[a].push(b);
    node[b].push(a);
}

for (let z=0; z<M; z++) {
    Sort(node[z]);
}

DFS(node, V, visited);
console.log(dfsOfList.join(" "))

for (let y=0; y<visited.length; y++) {
    visited[y] = false;
}

BFS(node, V, visited);
console.log(bfsOfList.join(" "));
