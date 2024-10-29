def merge_sort(array):
    if len(array) > 1:
        # Massivni ikkiga bo'lish
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        # Ikkala yarmini rekursiv ravishda qayta tartiblash
        merge_sort(left_half)
        merge_sort(right_half)

        # Indekslar
        i = j = k = 0

        # Birlashtirish
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Qolgan elementlarni qo'shish
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Sinov uchun massiv
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Saralangan massiv:", arr)
