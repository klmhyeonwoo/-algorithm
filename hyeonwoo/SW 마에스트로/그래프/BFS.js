const fs = require('fs');
const [n, m, v, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

const bfsOfList = []

function BFS(node, v, visited) {
    const queue = [v]; // 처음 큐라는 시작 예정인 요소들을 배열에 담아준다.
    visited[v] = true; // 방문 처리를 해준다.

    while (queue.length > 0) { // DFS에서는 재귀함수를 사용했지만, 여기서는 queue의 유무를 통해 반복문을 진행한다.
        let num = queue.shift(); // queue의 앞부분부터 원소를 제거해주면서 변수에 넣어준다.
        bfsOfList.push(num); // JS에서 출력을 위해 임의의 배열에 담아준다.
        for (let i of node[num]) { // node[원소]에 들어가서 요소들을 탐색한다.
            if (visited[i] === false) { // 만약 방문 기록이 false라면?
                queue.push(i); // queue에 넣어준다.
                visited[i] = true; // 그리고 그 방문 예정인 기록을 true로 만들어준다.
            }
        } 
    }
}

const N = parseInt(n); // 정점의 개수
const M = parseInt(m); // 간선의 개수
const V = parseInt(v); // 탐색을 시작할 정점의 번호

const ChangeNumList = arr => arr.map(Number);
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
    })
    return list;
}
const lst = ChangeNumList(arr);

let nodes = [];
let visited = [];

for (let i=0; i<=N; i++) {
    visited.push(false);
    nodes.push([]);
}

for (let k=0; k<lst.length; k+=2) {
    let a = lst[k];
    let b = lst[k+1];

    nodes[a].push(b);
    nodes[b].push(a);
}

for (let z=0; z<M; z++) {
    Sort(nodes[z]);
}

BFS(nodes, v, visited);
console.log(...bfsOfList)