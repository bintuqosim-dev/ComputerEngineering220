import Foundation


// Maximum Sum of Distinct Subarrays With Length K

// Sinxron


class MaxSumDistinctSubarraySync {
    
    func maxSumOfDistinctSubarrayWithLengthK(arr: [Int], k: Int) -> Int {
        guard arr.count >= k else
        { return 0 }
        
        var maxSum = 0
        var currentSum = 0
        var windowSet = Set<Int>() // Uniquenessni ta'minlash uchun

        for i in 0..<arr.count {
            // Windowni kengaytirish
            currentSum += arr[i]
            windowSet.insert(arr[i])
            
            // Window uzunligi K ga yetganda tekshiruv
            if i >= k - 1 {
                if windowSet.count == k { // Agar subarray unique bo'lsa
                    maxSum = max(maxSum, currentSum)
                }
                // Windowni chapga surish
                currentSum -= arr[i - k + 1]
                windowSet.remove(arr[i - k + 1])
            }
        }
        return maxSum
    }
}

// Asinxron

import Foundation

class MaxSumDistinctSubarrayAsync {
    
    func maxSumOfDistinctSubarrayWithLengthKAsync(arr: [Int], k: Int) async -> Int {
        guard arr.count >= k else { return 0 }
        
        var maxSum = 0
        var currentSum = 0
        var windowSet = Set<Int>() // Uniquenessni ta'minlash uchun

        for i in 0..<arr.count {
            // Windowni kengaytirish
            currentSum += arr[i]
            windowSet.insert(arr[i])
            
            // Window uzunligi K ga yetganda tekshiruv
            if i >= k - 1 {
                if windowSet.count == k { // Agar subarray unique bo'lsa
                    maxSum = max(maxSum, currentSum)
                }
                // Windowni chapga surish
                currentSum -= arr[i - k + 1]
                windowSet.remove(arr[i - k + 1])
            }
        }
        return maxSum
    }
}
