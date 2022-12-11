const fs = require('fs');
const [n, ...arr] = fs.readFileSync("nodeJS.txt").toString().trim().split(/\s/);

console.log(arr);