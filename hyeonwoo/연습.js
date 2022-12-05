lst = [1,6,43,7];

console.log(lst.sort((a,b) => {
    console.log(`a : ${a} b : ${b}, lst : ${lst}`);
    if (a > b) return 1; // a가 크다면 오름차순으로
    if (a < b) return -1; // b가 크다면 내림차순으로
}));