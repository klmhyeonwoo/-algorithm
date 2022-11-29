//
//  main.swift
//  CodingTestProject
//
//  Created by YoungK on 2022/11/27.
//

import Foundation

var n = 0
var m = 0
var nums = [Int]()

let s = readLine()!.split(separator: " ").map { Int($0)! }
n = s.first!
m = s.last!

// [1, 2, ..., n]
for i in 1...n { nums.append(i) }

/// nPr
func permutation(n elements: [Int], r: Int) -> [[Int]] {
    var result = [[Int]]()
    var visited = [Bool](repeating: false, count: n)
    
    func permu(_ temp: [Int]) {
        if temp.count == r {
            result.append(temp)
            return
        }
        
        for i in 0..<elements.count {
            if !visited[i] { // 중복 없도록 방문한 요소는 건너뛰기
                visited[i] = true
                permu(temp + [elements[i]])
                visited[i] = false
            }
        }
    }
    
    permu([])
    return result
}

let result = permutation(n: nums, r: m)
result.forEach {
    $0.forEach {
        print($0, terminator: " ")
    }
    print("")
}
