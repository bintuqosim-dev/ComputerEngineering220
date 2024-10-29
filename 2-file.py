# Bubble sort funksiyasi
def bubble_sort(massiv):
    n = len(massiv)
    # Har bir element uchun takrorlash
    for i in range(n):
        # Oxirgi qismi allaqachon saralangan
        for j in range(0, n - i - 1):
            # Agar j elementi j+1 elementidan katta bo'lsa, almashamiz
            if massiv[j] > massiv[j + 1]:
                massiv[j], massiv[j + 1] = massiv[j + 1], massiv[j]


# Misol uchun foydalanish
sonlar = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(sonlar)
print("Saralangan massiv:", sonlar)
