const fs = require('fs');
const [n, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const N = parseInt(n);
const nodes = [];
const visited = [];
let listOffirst = [];
const Sort = (list) => {
    list.sort((a,b) => {
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
const DFS = (nodes, v, visited) => {
    visited[v] = true;
    listOffirst.push(v);

    for (let i of nodes[v]) {
        if (visited[i] === false) {
            DFS(nodes, i, visited);
        }
    }
}

// console.log(arr);

for (let i=0; i<=N; i++) {
    nodes.push([]);
    visited.push(false);
}

for (let k=0; k<N; k++) {
    // console.log(arr);
    // console.log(arr.slice(0, arr.length / N))
    const item = arr.splice(0, 3);
    for (let z=1; z<item.length; z++) {
        if (item[z] !== `.`) {
            nodes[item[0].charCodeAt(0) - 64].push(item[z].charCodeAt(0) - 64);
            // nodes[item[z].charCodeAt(0) - 64].push(item[0].charCodeAt(0)-64);
        }
    }
}

for (let z=0; z<=N; z++) {
    Sort(nodes[z]);
}

// 전위 순회
DFS(nodes, 1, visited);
console.log(listOffirst);

// for (let a=0; a<visited.length; a++) {
//     visited[a] = false;
// }

console.log(nodes);

// listOffirst = [];
// console.log(listOffirst);

// DFS(nodes, 1, visited);

// console.log(listOffirst);


// console.log(nodes);

// const a = "A";
// console.log(a.charCodeAt(0) - 64);