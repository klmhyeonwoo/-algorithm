const fs = require('fs');
const [n, m, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const N = parseInt(n);
const M = parseInt(m);
const graph = [];
const log = [];
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let check = false;

function BFS(graph, x, y) {
    let count = 1;
    const queue = [];
    queue.push([x, y]);

    while (queue.length !== 0) {
        const item = queue.shift();
        const X = item[0];
        const Y = item[1];

        for (let i=0; i<4; i++) {
            const nx = X + dx[i];
            const ny = Y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
                continue
            }

            if (graph[nx][ny] === 1) {
                queue.push([nx, ny]);
                graph[nx][ny] = graph[X][Y] + 1;
                count += 1;
                // console.log(nx, ny, graph)
            }
        }
    }
    return count;       
}

for (let i of arr) {
    graph.push(i.split('').map(Number));
}

for (let x=0; x<N; x++) {

    for (let y=0; y<M; y++) {

        if (graph[x][y] === 1) {
            BFS(graph, x, y);
        }
    }
}

console.log(graph[N-1][M-1])