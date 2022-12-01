//
//  main.swift
//  CodingTestProject
//
//  Created by YoungK on 2022/11/27.
//

import Foundation

let n = Int(readLine()!)!
var arr = Array(repeating: Array(repeating: 0, count: n), count: n)
var visited = [Bool](repeating: false, count: n)
var result = Int.max

for i in 0..<n {
    arr[i] = readLine()!.split(separator: " ").map { Int($0)! }
}

func dfs(depth: Int, start: Int) {
    // depth 가 n/2 라는 뜻은 이미 한 팀 구성이 완료 됐다는 뜻
    // 그래서 depth/2 가 되면, 팀구성못한애들을(false) team2에 넣어줌!!
    if depth == n/2 {
        var team1 = 0
        var team2 = 0
        
        for i in 0..<n {
            for j in 0..<n {
                if !visited[i] && !visited[j] { // 방문안한 애들은 team2
                    team2 += arr[i][j]
                }
                if visited[i] && visited[j] { // 방문한 애들은 team1
                    team1 += arr[i][j]
                }
            }
        }
        //print("team1 능력치:", team1, "team2 능력치:", team2, "차이:", abs(team1 - team2))
        
        // 팀 간의 능력치 차이가 더 적으면 기존 result 와 업데이트
        result = min(result, abs(team1 - team2))
        return
    }
    
    // 탐색
    for i in start..<n {
        if !visited[i] {
            visited[i] = true
            dfs(depth: depth + 1, start: i)
            visited[i] = false
        }
    }
}

dfs(depth: 0, start: 0)
print(result)
