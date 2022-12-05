// [[80, 70], [90, 50], [40, 70], [50, 80]]	
// [1, 2, 4, 3]

function solution(score) {
    let scaledScore = [];
    let result = [];

    // 평균 값으로 배열을 재조정해줍니다.
    score.map((item) => {
        scaledScore.push(Math.round((item[0] + item[1])/2));
    });
    // console.log(scaledScore);

    let rankScore = scaledScore.slice(0, score.length);

    // 평균을 내림차순으로 만든 배열을 하나 만들어줍니다.
    rankScore.sort((a,b) => {
        if (a > b) return -1;
    });
    //console.log(rankScore);
    
    scaledScore.map((item) => {
        // console.log(`item의 값 : ${item}`);
        // console.log(scaledScore.indexOf(item));
        result.push(rankScore.indexOf(item) + 1);
    });
    
    return result
}

console.log(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]));