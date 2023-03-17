const fs = require('fs');
const [t, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);


const DFS = (nodes, v, visited) => {
    visited[v] = true;
    for (let i of nodes[v]) {
        if (visited[i] === false) {
            DFS(nodes, i, visited);
        }
    }
};

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
    });
    return list;
}

for (let i=0; i<t; i++) {

    let count = 0;

    const N = parseInt(arr.shift());
    const permutation = arr.splice(0, N).map(Number);
    const visited = [];
    const nodes = [];

    for (let k=0; k<=N; k++) {
        visited.push(false);
        nodes.push([]);
    }


    for (let z=1; z<=permutation.length; z++) {
        const a = permutation[z-1];

        nodes[z].push(a);
        // nodes[a].push(z);
    }

    // console.log(nodes)

    for (let e=0; e<=N; e++) {
        Sort(nodes[e]);
    }

    for (let c=1; c<visited.length; c++) {
        if (visited[c] === false) {
            // console.log(visited);
            DFS(nodes, c, visited);
            count += 1;
        }
    }
    
    console.log(count);
}
