function solution(num, total) {
    let answer = [];
    let sum = 0;
    for (let i=1; i<=num; i++) {
        answer.push(i);
    }

    sum = answer.reduce((a,b) => a + b, 0);
    if (total === sum) {
        return answer;
    } else if (total > sum) {
        while (true) {
            for (let i=0; i<num; i++) {
                answer[i] += 1
            }
    
            sum = answer.reduce((a,b) => a + b, 0);
            if (sum === total) {
                return answer;
            }
        }
    }
    else if (total < sum) {
        while (true) {
            for (let i=0; i<num; i++) {
                answer[i] -= 1
            }
    
            sum = answer.reduce((a,b) => a + b, 0);
            if (sum === total) {
                return answer;
            }
        }
    }
}

console.log(solution(5, 5));