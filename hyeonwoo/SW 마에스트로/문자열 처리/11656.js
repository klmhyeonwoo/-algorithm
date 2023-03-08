const fs = require('fs');
const [S] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

let lst = [];

const sort = (list) => {
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

for (let i=0; i<S.length; i++) {
    lst.push(S.slice(i, S.length));
}

for (let k of sort(lst)) {
    console.log(k);
}