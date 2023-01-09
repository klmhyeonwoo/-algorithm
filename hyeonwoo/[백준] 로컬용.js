const fs = require('fs');
const input = fs.readFileSync("nodeJS.txt").toString().trim().split(" ");

N = parseInt(input[0]);
L = parseInt(input[1]);

let lst = [];
let visited = [];
let result = [];

for (let i = 0; i <= N; i++) {
    visited.push(false);
}

// console.log(visited)

function permutation(size) {
    result = [];

    if (size === 3) {
        let answer = 0;
        console.log(lst)
        for (let k of lst) {
            result.push(k);
            for (let z of result) {
                answer += z;
            }
            if (answer === N) {
                break
            }
            return
        }
    }

    for (let k = 1; k <= N; k++) {
        if (visited[k] === false) {
            visited[k] = true;
            lst.push(k);
            permutation(size + 1);
            visited[k] = false;
            lst.pop();
        }

    }
}


permutation(0)

console.log(result);