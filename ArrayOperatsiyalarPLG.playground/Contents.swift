import Foundation

class InsertEndArr {
    
    init() {
        complete()
    }
    
    // Massivga element qo'shish funksiyasi
    func insertEnd(arr: inout [Int], n: Int, key: Int, capacity: Int) -> Int {
        // Agar massiv hajmi yetarli bo'lmasa, element qo'shib bo'lmaydi
        if n >= capacity {
            print("Cannot insert, array is full.")
            return n
        }
        
        arr.append(key) // Yangi elementni massivga qo'shamiz
        return n + 1 // Joriy hajmni qaytaramiz
    }
    
    func complete() {
        // Asosiy kod
        var arr = [12, 16, 20, 40, 50, 70] // Boshlang'ich massiv
        let capacity = 20 // Massivning maksimal hajmi
        var n = arr.count // Joriy o'lcham
        let key = 26 // Qo'shiladigan element
        
        print("Before Insertion: ", terminator: "")
        for i in 0..<n {
            print(arr[i], terminator: " ")
        }
        
        // Elementni qo'shish
        n = insertEnd(arr: &arr, n: n, key: key, capacity: capacity)
        
        print("\nAfter Insertion: ", terminator: "")
        for i in 0..<n {
            print(arr[i], terminator: " ")
        }
    }
}

let vc = InsertEndArr()
