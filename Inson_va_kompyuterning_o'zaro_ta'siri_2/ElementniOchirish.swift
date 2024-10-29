import UIKit
import Foundation

class ElementniOchirish {
    var arr = [10, 50, 30, 40, 20]
    let key = 30

    init() {
        print("Array before deletion")
        for element in arr {
            print(element, terminator: " ")
        }

        // Function call
        let n = deleteElement(arr: &arr, key: key)

        print("\n\nArray after deletion")
        for i in 0..<n {
            print(arr[i], terminator: " ")
        }
    }

    // Function to find the element's position without using `enumerated()`
    func findElement(arr: [Int], key: Int) -> Int? {
        for i in 0..<arr.count {
            if arr[i] == key {
                return i
            }
        }
        return nil
    }

    // Function to delete an element
    func deleteElement(arr: inout [Int], key: Int) -> Int {
        guard let pos = findElement(arr: arr, key: key) else {
            print("Element not found")
            return arr.count
        }
        
        for i in pos..<arr.count - 1 {
            arr[i] = arr[i + 1]
        }

        arr.removeLast()
        return arr.count
    }
}
