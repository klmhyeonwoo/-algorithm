//
//  PRG-크레인인형뽑기게임 .swift
//  CodingTestProject
//
//  Created by YoungK on 2023/01/16.
//

import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var board = board
    var stack = [Int]()
    var count = 0
    
    for line in moves {
        for row in 0..<board.count {
            if board[row][line-1] != 0 {
                let item = board[row][line-1] // 1. 인형 뽑기
                board[row][line-1] = 0
                
                if item == stack.last { // 2. 같으면 터짐
                    stack.removeLast()
                    count += 2
                } else {
                    stack.append(item) // 3. 다르면 바구니에 추가
                }
                
                break // moves 순서대로 뽑아야하므로
            }
        }
    }

    return count
}
