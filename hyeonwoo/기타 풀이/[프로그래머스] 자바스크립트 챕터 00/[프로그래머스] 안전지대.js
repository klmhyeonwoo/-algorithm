
// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,x,x,x,0]
// [0,x,1,x,0]
// [0,x,x,x,0]

// 25 - 9 = 16

// [0,0,0,0,0]
// [x,x,0,0,0]
// [1,x,0,0,0]
// [x,x,0,0,0]
// [0,0,0,0,0]

// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,x,x,x,0]
// [0,x,1,x,0]

// [0,0,0,0,0]
// [0,0,0,x,x]
// [0,0,0,x,1]
// [0,0,0,x,x]
// [0,0,0,0,0]

// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,x,x,x,x]
// [0,x,1,1,x]
// [0,x,x,x,x]

// [1,x,0,0,0]
// [x,x,0,0,0]
// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,0,0,0,0]

// [0,0,0,0,0]
// [x,x,0,0,0]
// [1,x,0,0,0]
// [x,x,0,0,0]
// [1,1,1,1,1]

// [0,0,0,x,1]
// [0,0,0,x,x]
// [0,0,0,0,0]
// [0,0,0,0,0]
// [0,0,0,0,0]

function solution(board) {
    for (let i=0; i<board.length; i++) {
        for (let k=0; k<board[i].length; k++) {
            // 1이 세로 index 0에서 발견될 경우
            if (board[i][k] === 1 && k === 0) {
                if (i === 0) {
                    if (board[i][k+1] !== 1) {
                        board[i][k+1] = 3;
                    }
                    if (board[i+1][k] !== 1) {
                        board[i+1][k] = 3;
                    }
                    if (board[i+1][k+1] !== 1) {
                        board[i+1][k+1] = 3;
                    }
                }
                else if (i === board.length-1) {
                    if (board[i][k+1] !== 1) {
                        board[i][k+1] = 3
                    }
                    if (board[i-1][k] !== 1) {
                        board[i-1][k] = 3;
                    }
                    if (board[i-1][k+1] !== 1) {
                        board[i-1][k+1] = 3;
                    }
                }
                else {                    
                    if (board[i][k+1] !== 1) {
                        board[i][k+1] = 3
                    }
                    if (board[i+1][k] !== 1) {
                        board[i+1][k] = 3;
                    }
                    if (board[i+1][k+1] !== 1) {
                        board[i+1][k+1] = 3;
                    }
                    if (board[i-1][k] !== 1) {
                        board[i-1][k] = 3;
                    }
                    if (board[i-1][k+1] !== 1) {
                        board[i-1][k+1] = 3;
                    }
                }
            }
            // 1이 세로 index 마지막에서 발견될 경우
            else if (board[i][k] === 1 && k === board[i].length-1) {
                if (i === 0) {
                    if (board[i][k-1] !== 1) {
                        board[i][k-1] = 3;
                    }
                    if (board[i+1][k] !== 1) {
                        board[i+1][k] = 3;
                    }
                    if (board[i+1][k-1] !== 1) {
                        board[i+1][k-1] = 3;
                    }
                }
                else if (i === board.length) {
                    if (board[i][k-1] !== 1) {
                        board[i][k-1] = 3;
                    }
                    if (board[i-1][k] !== 1) {
                        board[i-1][k] = 3;
                    }
                    if (board[i-1][k-1] !== 1) {
                        board[i-1][k-1] = 3;
                    }
                }
                else {
                    if (board[i][k-1] !== 1) {
                        board[i][k-1] = 3;
                    }
                    if (board[i-1][k] !== 1) {
                        board[i-1][k] = 3;
                    }
                    if (board[i-1][k-1] !== 1) {
                        board[i-1][k-1] = 3;
                    }
                    if (board[i-1][k] !== 1) {
                        board[i-1][k] = 3;
                    }
                    if (board[i-1][k-1] !== 1) {
                        board[i-1][k-1] = 3;
                    }
                }
            } else if (board[i][k] === 1) {
                if (k >= 1 && k <= board[i].length-2) {
                    if (i === 0) {
                        if (board[i][k-1] !== 1) {
                            board[i][k-1] = 3;
                        }
                        if (board[i][k+1] !== 1) {
                            board[i][k+1] = 3;
                        }
                        if (board[i+1][k] !== 1) {
                            board[i+1][k] = 3;
                        }
                        if (board[i+1][k-1] !== 1) {
                            board[i+1][k-1] = 3;
                        }
                        if (board[i+1][k+1] !== 1) {
                            board[i+1][k+1] = 3;
                        }
                    }

                    else if (i === board.length-1) {
                        if (board[i][k-1] !== 1) {
                            board[i][k-1] = 3;
                        }
                        if (board[i][k+1] !== 1) {
                            board[i][k+1] = 3;
                        }
                        if (board[i-1][k] !== 1) {
                            board[i-1][k] = 3;
                        }
                        if (board[i-1][k-1] !== 1) {
                            board[i-1][k-1] = 3;
                        }
                        if (board[i-1][k+1] !== 1) {
                            board[i-1][k+1] = 3;
                        }
                    }

                    else {
                        if (board[i][k-1] !== 1) {
                            board[i][k-1] = 3;
                        }
                        if (board[i][k+1] !== 1) {
                            board[i][k+1] = 3;
                        }
                        if (board[i+1][k] !== 1) {
                            board[i+1][k] = 3;
                        }
                        if (board[i+1][k-1] !== 1) {
                            board[i+1][k-1] = 3;
                        }
                        if (board[i+1][k+1] !== 1) {
                            board[i+1][k+1] = 3;
                        }
                        if (board[i-1][k] !== 1) {
                            board[i-1][k] = 3;
                        }
                        if (board[i-1][k-1] !== 1) {
                            board[i-1][k-1] = 3;
                        }
                        if (board[i-1][k+1] !== 1) {
                            board[i-1][k+1] = 3;
                        }
                    }
                }
            }
        }
    }

    let size = board.length * board[0].length;
    let count = 0;

    board.map((item) => {
        console.log(item);
        for(let z of item) {
            if (z === 1 || z === 3) {
                count += 1;
            }
        }
    })

    let result = size - count;

    return result;
}

console.log(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))