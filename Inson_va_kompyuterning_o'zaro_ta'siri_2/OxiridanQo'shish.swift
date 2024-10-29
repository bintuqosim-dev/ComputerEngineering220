//
//  OxiridanQo'shish.swift
//  Inson_va_kompyuterning_o'zaro_ta'siri_2
//
//  Created by Diyorbek Xikmatullayev on 29/10/24.
//

import Foundation

class InsertEnd {
     
    init() {
        main()
    }
    
  
    // Massivga element kiritish funksiyasi
    func insertEnd(arr: inout [Int], n: Int, key: Int, capacity: Int) -> Int {
        // Agar massiv hajmi yetarli bo'lmasa, element qo'shib bo'lmaydi
        if n >= capacity {
            return n
        }

        // Oxirgi joyga elementni qo'shish
        arr[n] = key
        return n + 1
    }

    // Asosiy dastur
    func main() {
        var arr = [12, 16, 20, 40, 50, 70]
        lazy var arrCap = arr + Array(repeating: 0, count: 14) // Maksimal hajmi 20 bo'lgan massiv
        let capacity = arrCap.count
        lazy var n = arr.count
        let key = 26

        print("\nBefore Insertion: ", terminator: "")
        for i in 0..<n {
            print(arrCap[i], terminator: " ")
        }

        // Elementni qo'shish
        n = insertEnd(arr: &arrCap, n: n, key: key, capacity: capacity)

        print("\nAfter Insertion: ", terminator: "")
        for i in 0..<n {
            print(arrCap[i], terminator: " ")
        }
    }
}
