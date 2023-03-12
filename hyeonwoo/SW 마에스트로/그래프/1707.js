const fs = require('fs');
const [...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split('\n');

let listOfDFS = [];
let listOfBFS = [];
const RED = -1;
const BLUE = 1;
let state = true;
const K = arr.shift() // 몇번의 테스트 케이스를 활용할 것인지
const Sort = (list) => { // 직접 구현한 sort 오름차순 함수
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

const BFS = (nodes, v, visited) => {
    visited[v] = "blue";
    let queue = [v];
    while (queue.length > 0) {
        let start = queue.shift();
        for (let i of nodes[start]) {
            if (visited[i] === false) {
                queue.push(i);
                visited[i] = true;
            }
        }
    }
}

const DFS = (nodes, v, visited, color) => { // 직접 구현한 DFS 함수
    visited[v] = color;
    listOfDFS.push(v);
    for (let i of nodes[v]) {
        if (visited[i] === color) {
            state = false;
            return;
        }

        if (visited[i] === 0) {
            DFS(nodes, i, visited, -color);
        }
    }
};

// console.log(arr);
for (let i=0; i<K; i++) {
    const nodes = [];
    const visited = [];
    state = true;
    listOfDFS = [];

    const [V, E] = arr.shift().split(' ').map(Number);
    const edges = arr.splice(0, E).map((v) => {
        return v.split(' ').map(Number)
    }); // 순회하면서 숫자로 바꿔줍니다.

    for (let k=0; k<=V; k++) { // nodes에는 요소들이 들어갈 빈 배열을, visited에는 방문 기록을 남길 요소들을 만듭니다.
        nodes.push([]);
        visited.push(0);
    }

    for (let z=0; z<E; z++) {
        const a = edges[z][0];
        const b = edges[z][1];

        nodes[a].push(b);
        nodes[b].push(a);
    }

    for (let e=0; e<=V; e++) {
        Sort(nodes[e]);
    }

    for (let q=1; q<=V; q++) {
        if (!state) {
            break;
        }
        if (visited[q] === 0) {
            DFS(nodes, q, visited, RED);
        }
    }

    // console.log(visited, state)
    // 결과 출력
    if (state === true) {
        console.log("YES");
    } else {
        console.log("NO");
    }
}