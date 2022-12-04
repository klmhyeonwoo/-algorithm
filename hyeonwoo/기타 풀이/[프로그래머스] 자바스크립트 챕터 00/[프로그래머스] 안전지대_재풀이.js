function solution(board) {

    // 전체 순회
    for(let i = 0 ; i < board.length ; i ++) {
        for(let j = 0 ; j < board[i].length ; j ++) {
            // board[i][j]의 값이 1인경우 상하좌우 및 대각선 검사를 실행
            if(board[i][j] === 1) {
                // 상하 좌우를 2로 변경하되 이는 해당 칸이 0인 경우에만 해당 즉 폭탄은 건들지 않는다.
                // 맨 윗줄이 아닌 경우
                if(i !== 0 && board[i-1][j] !== 1) {
                    // console.log("1")
                    board[i-1][j] = 2    
                }
                // 맨 아랫줄이 아닌 경우
                if(i !== board.length-1 && board[i+1][j] !== 1) {
                    // console.log("2")
                    board[i+1][j] = 2
                }
                // 맨 왼쪽이 아닌 경우
                if(j !== 0 && board[i][j-1] !== 1) {
                    // console.log("3")
                    board[i][j-1] = 2
                }
                // 맨 오른쪽이 아닌 경우
                if(j !== board[i].length-1 && board[i][j+1] !== 1) {
                    // console.log("4")
                    board[i][j+1] = 2
                }
                // 맨 대각선 윗 왼쪽이 아닌 경우
                if(i !== 0 && j !== 0 && board[i-1][j-1] !== 1) {
                    // console.log("5")
                    board[i-1][j-1] = 2
                }
                // 맨 대각선 윗 오른쪽이 아닌 경우
                if(i !== 0 && j !== board[i].length-1 && board[i-1][j+1] !== 1) {
                    // console.log("6")
                    board[i-1][j+1] = 2
                }
                // 맨 대각선 아랫 왼쪽이 아닌 경우
                if(i !== board.length-1 && j !== 0 && board[i+1][j-1] !== 1) {
                    // console.log("7")
                    board[i+1][j-1] = 2
                }
                // 맨 대각선 아랫 오른쪽이 아닌 경우
                if(i !== board.length-1 && j !== board[i].length-1 && board[i+1][j+1] !== 1) {
                    // console.log("8")
                    board[i+1][j+1] = 2
                }
            }
        }
    }

    let result = board.length * board[0].length;
    let count = 0;
    board.map((item) => {
        for (let k of item) {
            if (k === 1 || k === 2) {
                count += 1;
            }
        }
    })

    return result - count;
}

console.log(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))

// 참고 : https://velog.io/@kwb020312/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%88%EC%A0%84%EC%A7%80%EB%8C%80