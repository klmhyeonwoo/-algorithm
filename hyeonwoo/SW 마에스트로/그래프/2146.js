const fs = require('fs');
const [n, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const N = parseInt(n);
const graph = [];
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let label = 2;
let res = parseInt(1e9);


// 섬 구분 라벨링 함수
const BFS = (graph, x, y) => {
    const queue = [];
    queue.push([x,y]);
    graph[x][y] = label;
    
    while (queue.length !== 0) {
        const item = queue.shift();
        const X = item[0];
        const Y = item[1];

        // console.log(item);

        for (let i=0; i<4; i++) {
            const nx = X + dx[i];
            const ny = Y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                continue;
            }

            // console.log(nx, ny);

            if (graph[nx][ny] === 1) {
                queue.push([nx,ny]);
                graph[nx][ny] = label;
            }
        }
    }

    return;
}

// 최단 거리 구하기 BFS 알고리즘
const BFS2 = (v) => {
    const queue = [];
    const dist = [];

    for (let i=0; i<N; i++) {
        const item = [];
        for (let z=0; z<N; z++) {
            item.push(-1);
        }
        dist.push(item);
    }

    for (let x=0; x<N; x++) {
        for (let y=0; y<N; y++) {
            if (graph[x][y] === v) {
                dist[x][y] = 0;
                queue.push([x, y]);
            }
        }
    }

    while (queue.length !== 0) {
        const item = queue.shift();
        const X = item[0];
        const Y = item[1];

        for (let i=0; i<4; i++) {
            const nx = X + dx[i];
            const ny = Y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                continue;
            } 

            if (graph[nx][ny] && graph[nx][ny] !== v) {
                // console.log(dist[nx]);
                return dist[X][Y];
            } else if (!graph[nx][ny] && dist[nx][ny] === -1) {
                dist[nx][ny] = dist[X][Y] + 1;
                queue.push([nx, ny]);
            }
        }
    }
    return parseInt(1e9);
}

for (let i=0; i<N; i++) {
    graph.push(arr.splice(0, N).map(Number));
}

// 섬 구분
for (let x=0; x<N; x++) {
    for (let y=0; y<N; y++) {
        if (graph[x][y] === 1) {
            BFS(graph, x, y);
            label += 1;
        }
    }
}

// 최단 거리를 구해봅시다.
for (let k=1; k<label; k++) {
    res = Math.min(res, BFS2(k));
}

// console.log(graph)
console.log(res);