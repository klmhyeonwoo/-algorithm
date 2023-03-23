const fs = require('fs');
const [...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split('\n');

/* 
000
0x0
000
*/

const item = arr[0].split(' ').map(Number);
const N = item[0]; // 세로칸
const M = item[1]; // 가로칸
const graph = [];
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let result = 0;
const queue = [];

function BFS() {
    while (queue.length !== 0) {
        const item = queue.shift();
        const A = item[0];
        const B = item[1];
        
        for (let i=0; i<dx.length; i++) {
            const nx = A + dx[i];
            const ny = B + dy[i];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
                continue;
            }

            if (graph[nx][ny] === 0) {
                graph[nx][ny] = graph[A][B] + 1;
                queue.push([nx, ny]);
            }
        }
    }
}

for (let i of arr.splice(1)) {
    graph.push(i.split(' ').map(Number));
}

for (let x=0; x<M; x++) {
    for (let y=0; y<N; y++) {
        if (graph[x][y] === 1) {
            queue.push([x, y]);
        }
    }
}

BFS();

for (let k of graph) {
    if (k.includes(0)) {
        result = -1;
        break;
    }
    result = Math.max(result, ...k);
}

if (result === -1) {
    console.log(result);
} else {
    console.log(result-1);
}
