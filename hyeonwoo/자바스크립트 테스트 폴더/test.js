let a = { name: "hyeonwoo" }
let b = Object.assign({}, a);

b.name = "minwoo";

console.log(a);
console.log(b);