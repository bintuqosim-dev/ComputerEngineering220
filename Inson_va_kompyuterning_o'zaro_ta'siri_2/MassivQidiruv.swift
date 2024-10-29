import UIKit
import Foundation

class LinearSearch {
    let arr = [12, 34, 10, 6, 40]
    let key = 40

    init() {
        
        if let position = findElement(arr: arr, key: key) {
            print("\nElement Found at Position: \(position + 1)")
        } else {
            print("\nElement not found")
        }
    }
    
    // Elementni qidirish funksiyasi
    func findElement(arr: [Int], key: Int) -> Int? {
        for i in 0..<arr.count {
            if arr[i] == key {
                return i
            }
        }
        // Agar element topilmasa
        return nil
    }
}

// Asosiy qism


