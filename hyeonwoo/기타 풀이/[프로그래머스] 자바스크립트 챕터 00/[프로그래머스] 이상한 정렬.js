function solution(numlist, n) {
    // 오름차순: 작은 것부터 큰 것으로 가는 순서 
    // 내림차순: 큰 것으로부터 작은 것으로 가는 순서
    lst = [1,2,3,4]

    lst.sort((a,b) => {
        console.log(a, b, b-a)
        // -1이면 내림차순
        console.log(a, b, a-b)
        // 1이면 오름차순
        return a-b;
    });

    console.log(lst);

    return numlist.sort((a, b)=> {
        const [A, B] = [Math.abs(n-a), Math.abs(n-b)];
        if (A === B) {
            return b-a;
        }
        console.log(`a : ${a}, b: ${b}, A: ${A}, B: ${B}`);
        return A-B;
    });
}

console.log(solution([1,2,3,4,5,6],4));