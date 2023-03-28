const fs = require('fs');
const [n, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split("\n");

let tree = {};

arr.forEach((items) => {
    const item = items.split(' ');
    const data = item[0];
    const left = item[1] === `.` ? null : item[1];
    const right = item[2] === `.` ? null : item[2];

    tree[data] = {left, right};
})

let answer = ['', '', ''];

// 전위순회는 루트 - 왼쪽 - 오른쪽 방식으로 
function preOrder(node) {
    if (node !== null) {
        answer[0] += node;
        preOrder(tree[node].left);
        preOrder(tree[node].right);
    }
}

// 중위순회는 왼쪽 - 루트 - 오른쪽 방식으로
function inOrder(node) {
    if (node !== null) {
        inOrder(tree[node].left);
        answer[1] += node;
        inOrder(tree[node].right);
    }
}

// 후위 순위는 왼쪽 - 오른쪽 - 루트 방식으로
function postOrder(node) {
    if(node !== null) {
        postOrder(tree[node].left);
        postOrder(tree[node].right);
        answer[2] += node;
    }
}

preOrder('A');
inOrder('A');
postOrder('A');

console.log(answer[0])
console.log(answer[1])
console.log(answer[2])