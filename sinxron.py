def maximumSubarraySum(nums, k):
    n = len(nums)
    max_sum = 0
    current_sum = 0
    window = set()  # Takrorlanmas elementlarni saqlash uchun
    left = 0  # Sliding windowning chap tomoni

    for right in range(n):
        # Takrorlanadigan elementlarni olib tashlash
        while nums[right] in window:
            window.remove(nums[left])
            current_sum -= nums[left]
            left += 1

        # Yangi elementni oynaga qo'shish
        window.add(nums[right])
        current_sum += nums[right]

        # Oynaning uzunligi K ga yetganda, maksimumni yangilash
        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            # Oynani siljitish
            window.remove(nums[left])
            current_sum -= nums[left]
            left += 1

    return max_sum


# Misol uchun:
nums = [4, 2, 4, 5, 6]
k = 3
result = maximumSubarraySum(nums, k)
print(f"Sinxron natija: {result}")  # Output: 15