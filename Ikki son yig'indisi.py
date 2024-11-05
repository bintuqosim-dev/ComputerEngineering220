def yigindi(a, b):
    try:
        # Sonlarni float ga aylantirib tekshiramiz
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        # Agar kiritilgan qiymat son bo'lmasa
        return "Iltimos, faqat son kiriting."

son1 = input("Birinchi sonni kiriting: ")
son2 = input("Ikkinchi sonni kiriting: ")

# Funksiyani chaqirish va natijani chiqarish
natija = yigindi(son1, son2)
print("Yig'indi:", natija)

