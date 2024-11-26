import time

# SMS yuborishni taqlid qiluvchi funksiya
def sms_yubor_sinxron(raqam):
    print(f"{raqam} raqamiga SMS yuborilmoqda...")
    time.sleep(2)  # SMS yuborishni taqlid qilish
    print(f"{raqam} raqamiga SMS yuborildi.")

# Do'stlarning telefon raqamlari
raqamlar = ["+998901234567", "+998909876543", "+998931234567"]

# Sinxron SMS yuborish funksiyasi
def sinxron_sms_yuborish():
    for raqam in raqamlar:
        sms_yubor_sinxron(raqam)

start = time.time()
sinxron_sms_yuborish()
end = time.time()
print(f"Sinxron usulda bajarildi: {end - start:.2f} soniya")
