function solution(lines) {
    answer = 0;

    let obj = {};

    for (const LINE of lines) {
        const [X, Y] = LINE;

        const START = Math.min(X, Y);
        const END = Math.max(X, Y);

        for (let i= START; i < END; i++) {
            obj[i] = obj[i] + 1 || 1;
        }
        //console.log("hi!", obj);
    }
    
    const RESULT = Object.values(obj).filter((num) => num >= 2).length;
    return RESULT;
}

console.log(solution([[0, 5], [3, 9], [1, 10]]));