const permutation = (size, M) => {
    // 이게 순열이라는거구나,,
    // 하나씩 size 값을 올려주면서, 개수와 size값이 같으면 재귀 종료
    if (size === M) {
        console.log(lst.join(" "));
        return
    }

    for (let k=1; k<=N; k++) {
        if (visited[k] === false) {
            visited[k] = true;
            lst.push(k);
            permutation(size + 1, M);
            visited[k] = false;
            lst.pop();
        }
    }
}

const N = 4;
const M = 2;
let visited = [];
let lst = [];

for (let i=0; i<=N; i++) {
    visited.push(false);
}

permutation(0, M);

//console.log(visited);