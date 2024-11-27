// Maximum Sum of Distinct Subarrays With Length K

// MARK - Sinxron

import Foundation

class MaxSumDistinctSubarraySync {
    
    func maxSumOfDistinctSubarrayWithLengthK(arr: [Int], k: Int) -> Int {
        guard arr.count >= k else {
            print("Massiv uzunligi \(k) dan kichik, natija 0.")
            return 0
        }
        
        var maxSum = 0
        var currentSum = 0
        var windowSet = Set<Int>() // Uniquenessni ta'minlash uchun

        for i in 0..<arr.count {
            print("Element qo'shilmoqda: \(arr[i])")
            currentSum += arr[i]
            windowSet.insert(arr[i])
            Thread.sleep(forTimeInterval: 2) // 2 sekund kutish

            // Window uzunligi K ga yetganda tekshiruv
            if i >= k - 1 {
                print("Tekshirilmoqda: Window: \(Array(arr[i-k+1...i]))")
                if windowSet.count == k { // Agar subarray unique bo'lsa
                    maxSum = max(maxSum, currentSum)
                    print("Yangi maksimum topildi: \(maxSum)")
                }
                // Windowni chapga surish
                print("Windowni chapga surish: O'chirilayotgan element: \(arr[i - k + 1])")
                currentSum -= arr[i - k + 1]
                windowSet.remove(arr[i - k + 1])
                Thread.sleep(forTimeInterval: 2) // 2 sekund kutish
            }
        }
        
        print("Natija: Maksimal summa \(maxSum)")
        return maxSum
    }
}

// Sinov
let arr = [4, 3, 2, 4, 5, 1, 2]
let k = 3

let calculator = MaxSumDistinctSubarraySync()
let result = calculator.maxSumOfDistinctSubarrayWithLengthK(arr: arr, k: k)
print("Final Maksimum: \(result)")


// MARK - Asinxron

import Foundation

class MaxSumDistinctSubarrayAsync {
    
    func maxSumOfDistinctSubarrayWithLengthKAsync(arr: [Int], k: Int) async -> Int {
        guard arr.count >= k else {
            print("Massiv uzunligi \(k) dan kichik, natija 0.")
            return 0
        }
        
        var maxSum = 0
        var tasks: [Task<Int, Never>] = []

        for i in 0..<arr.count - k + 1 {
            // Parallel hisoblash uchun Task yaratamiz
            let task = Task { () -> Int in
                let subarray = Array(arr[i..<i+k])
                let uniqueSet = Set(subarray)
                if uniqueSet.count == k {
                    let sum = subarray.reduce(0, +)
                    print("Subarray: \(subarray), Sum: \(sum)")
                    return sum
                }
                return 0
            }
            tasks.append(task)
        }
        
        // Barcha Task'larni natijasini kutish
        for task in tasks {
            let result = await task.value
            maxSum = max(maxSum, result)
        }
        
        print("Natija: Maksimal summa \(maxSum)")
        return maxSum
    }
}

// Sinov
let arrA = [4, 3, 2, 4, 5, 1, 2]
let kA = 3

let calculatorA = MaxSumDistinctSubarrayAsync()

Task {
    let result = await calculatorA.maxSumOfDistinctSubarrayWithLengthKAsync(arr: arrA, k: kA)
    print("Final Maksimum: \(result)")
}

// Asosiy oqim tugashini kutish
RunLoop.current.run(until: Date().addingTimeInterval(5))
