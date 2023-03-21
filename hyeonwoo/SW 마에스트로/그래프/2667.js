const fs = require('fs');
const [a, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

let A = parseInt(a);
const graph = [];
const result = [];
const dx = [0, 0, 1, -1];
const dy = [-1, 1, 0, 0];

const functionOfSort = (list) => {
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

const BFS = (graph, x, y) => {
    const queue = [];
    queue.push([x, y]);
    let count = 1;
    graph[x][y] = 0;


    while (queue.length !== 0) {
        const item = queue.shift();

        // let X, Y = item;
        // console.log(typeof item);

        const X = item[0];
        const Y = item[1];

        for (let i=0; i<4; i++) {
            const nx = X + dx[i];
            const ny = Y + dy[i];

            if (nx < 0 || nx >= A || ny < 0 || ny >= A) {
                continue;
            }

            if (graph[nx][ny] === 1) {
                graph[nx][ny] = 0;
                queue.push([nx, ny]);
                count += 1;
            }
        }
    }
    return count;
}

for (let i=0; i<arr.length; i++) {
    graph.push(arr[i].split('').map(Number));
}

for (let x=0; x<graph.length; x++) {
    for (let y=0; y<graph.length; y++) {
        if (graph[x][y] === 1) {
            result.push(BFS(graph, x, y));
        }
    }
}

functionOfSort(result);
console.log(result.length);
for (let z of result) {
    console.log(z);
}