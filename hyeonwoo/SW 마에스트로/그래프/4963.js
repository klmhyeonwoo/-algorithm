const fs = require('fs');
const [...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split('\n');

/* 
000
000
000
*/

const dx = [-1, 1, 0, 0, -1, 1, 1, -1];
const dy = [0, 0, -1, 1, 1, 1, -1, -1];
const result = [];

while (1) {

    function BFS(graph, x, y) {
        const queue = [];
        queue.push([x, y]);
        graph[x][y] = 0;
        
        while (queue.length !== 0) {
            const item = queue.shift();
            const a = item[0];
            const b = item[1];
            
            for (let i=0; i<dx.length; i++) {
                const nx = a + dx[i];
                const ny = b + dy[i];
    
                if (nx < 0 || nx >= height || ny < 0 || ny >= width) {
                    continue;
                }
    
                if (graph[nx][ny] === 1) {
                    graph[nx][ny] = 0;
                    queue.push([nx, ny]);
                }
            }
        }
    
        return;
    }

    const lst = arr.splice(0,1)[0].split(' ').map(Number);
    const width = lst[0];
    const height = lst[1];
    const Tcase = [];
    const T = arr.splice(0, height);
    let count = 0;

    if (width === 0 && height === 0) {
        break;
    }

    // console.log(width, height, T);

    for (let i of T) {
        Tcase.push(i.split(' ').map(Number));
    }

    // console.log(Tcase);
    
    for (let y=0; y<height; y++) {
        for (let x=0; x<width; x++) {
            if (Tcase[y][x] === 1) {
                count += 1;
                BFS(Tcase, y, x);
            }
        }
    }

    result.push(count);
}

// console.log(result);

for (let i of result) {
    console.log(i);
}