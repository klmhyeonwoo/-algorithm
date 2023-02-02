//
//  PRG-개인정보수집유효기간.swift
//  CodingTestProject
//
//  Created by YoungK on 2023/02/02.
//

import Foundation

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    var result: [Int] = []
    var dict: [String: Int] = [:]
    
    // 유효기간 딕셔너리 생성 ex) [A:6], [B:12], ...
    terms.forEach { dict.updateValue(Int($0.split(separator: " ").last!)!,
                                 forKey: String($0.split(separator: " ").first!)) }
    
    // 1. 비교하기 편하도록 현재날짜를 일수로 계산
    let convertedToday = convert(today)
    
    for i in 0..<privacies.count {
        let item = privacies[i].split(separator: " ")
        
        // 2. 현재 개인정보의 수집일을 일수로 계산
        let convertedPrivacy = convert(String(item.first!))
        
        // 3. 유효기간 딕셔너리에서 유효기간을 꺼내 일수로 계산
        let validDays = dict[String(item.last!)]! * 28
        
        // 4. 현재 날짜가 개인정보 수집일 + 유효기간 보다 같거나 지났으면 파기합니다.
        if convertedToday >= convertedPrivacy + validDays { result.append(i+1) }
    }
    
    return result
}

func convert(_ date: String) -> Int {
    let a = date.split(separator: ".").map { Int($0)! }
    let year = a[0]
    let month = a[1]
    let day = a[2]
    return (year * 12 * 28) + (month * 28) + day
}
