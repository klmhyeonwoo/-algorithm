const fs = require('fs');
const [t, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const ChangeNumList = (list) => list.map(Number);
const T = parseInt(t);
let listOfDFS = [];
let count = 0;

const DFS = (nodes, v, visited) => {
    visited[v] = true;
    listOfDFS.push(v);
    if (visited[nodes[v]]) {
        if (listOfDFS.includes(nodes[v])) {
            count += listOfDFS.slice(listOfDFS.indexOf(nodes[v])).length;
        }
        return
    } else {
        DFS(nodes, nodes[v], visited);
    }
}


for (let i=0; i<T; i++) {
    const N = parseInt(arr.shift());
    const lst = ChangeNumList(arr.splice(0, N));
    const visited = [];
    const nodes = [0];
    count = 0;
    
    for (let k=0; k<=N; k++) {
        visited.push(false);
    }

    for(let z=1; z<=lst.length; z++) {
        nodes.push(lst[z-1]);
    }

    // console.log(nodes);

    for(let y=1; y<=visited.length; y++) {
        if (visited[y] === false) {
            listOfDFS = [];
            DFS(nodes, y, visited);
        }
    }

    console.log(N - count);
}