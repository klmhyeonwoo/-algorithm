const fs = require('fs');
const [t, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const ChangeNumList = (list) => list.map(Number);
const T = parseInt(t);
let listOfDFS = [];

const DFS = (nodes, v, visited) => {
    visited[v] = true;
    for (let i of nodes[v]) {
        listOfDFS.push(i);
        if (visited[i] === false) {
            DFS(nodes, i, visited)
        }
    }
}

for (let i=0; i<T; i++) {
    const N = parseInt(arr.shift());
    const lst = ChangeNumList(arr.splice(0, N));
    const visited = [];
    const nodes = [];
    let count = 0;
    
    for (let k=0; k<=N; k++) {
        visited.push(false);
        nodes.push([]);
    }

    for(let z=1; z<=lst.length; z++) {
        nodes[z].push(lst[z-1]);
    }

    for(let y=1; y<visited.length; y++) {
        listOfDFS = [];

        if (visited[y] === false) {
            DFS(nodes, y, visited);
        }
        
        if (listOfDFS[listOfDFS.length-1] !== y) {
            for (let z of listOfDFS) {
                visited[z] = false;
            }
            // console.log("셈이 안되는 친구들 : ", y, listOfDFS)
        } else {
            // console.log("셈이 되는 친구들 : ", y, listOfDFS)
            count += listOfDFS.length;
        }
    }
    console.log(N - count);
}