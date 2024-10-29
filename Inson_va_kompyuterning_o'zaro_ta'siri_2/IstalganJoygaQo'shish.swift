//
//  IstalganJoygaQo'shish.swift
//  Inson_va_kompyuterning_o'zaro_ta'siri_2
//
//  Created by Diyorbek Xikmatullayev on 29/10/24.
//

import Foundation

class insertElementAnyPosition {
    
    init() {
        useFunk()
    }
    
    func insertElement(arr: inout [Int], n: Int, x: Int, pos: Int) {
        // Pozitsiyadan keyingi elementlarni o'ngga siljitish
        var i = n - 1
        while i >= pos {
            arr[i + 1] = arr[i]
            i -= 1
        }
        
        // Yangi elementni qo'shish
        arr[pos] = x
    }

    func useFunk() {
        var arr = [2, 4, 1, 8, 5] + Array(repeating: 0, count: 10) // Massiv hajmini oldindan belgilab qo'yamiz
        var n = 5

        print("\nBefore insertion: ", terminator: "")
        for i in 0..<n {
            print(arr[i], terminator: " ")
        }
        print()

        let x = 10, pos = 2

        // Funksiya chaqiruvi
        insertElement(arr: &arr, n: n, x: x, pos: pos)
        n += 1

        print("\nAfter insertion: ", terminator: "")
        for i in 0..<n {
            print(arr[i], terminator: " ")
        }
    }



}

