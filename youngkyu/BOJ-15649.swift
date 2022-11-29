//
//  main.swift
//  CodingTestProject
//
//  Created by YoungK on 2022/11/27.
//
 
import Foundation

let nm = readLine()!.split(separator: " ").map { Int($0)! }
let n = nm.first!
let m = nm.last!
let nums = Array(1...n) // [1, 2, ..., n]

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
    $0.forEach { print($0, terminator: " ") }
    print("")
}
