//
//  main.swift
//  CodingTestProject
//
//  Created by YoungK on 2022/11/27.
//
 
import Foundation

let n = Int(readLine()!)!
let arrowR = [-1, 1, 0, 0] // 상 하 좌 우
let arrowC = [0, 0, -1, 1] // 상 하 좌 우
var graph = [[Int]]()
for _ in 0..<n {
    graph.append(readLine()!.map{ Int(String($0))! })
}

//_ = graph.map{ print($0) }
//print("--------------------")

func bfs(_ r: Int, _ c: Int) -> Int {
    var queue: [(r: Int, c: Int)] = [(r,c)]
    graph[r][c] = 0 // 방문 처리
    var index = 0
    var count = 1
    
    while queue.count > index {
        let node = queue[index] // 큐에서 하나를 꺼냄
        index += 1
        
        for i in 0..<4 {
            let (nr, nc) = (node.r+arrowR[i], node.c+arrowC[i])
            if !((0..<n).contains(nr) && (0..<n).contains(nc)) { continue } // 예외 처리
            if graph[nr][nc] == 1 {
                graph[nr][nc] = 0
                count += 1
                queue.append((nr, nc))
            }
        }
    }
//    _ = graph.map{ print($0) }
//    print("--------------------")
    return count
}

var aptList: [Int] = []

for i in 0..<n {
    for j in 0..<n {
        if graph[i][j] == 1 {
            aptList.append(bfs(i, j))
        }
    }
}

print(aptList.count)
aptList.sorted(by: <).forEach { print($0) }
