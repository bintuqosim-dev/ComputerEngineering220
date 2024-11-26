import asyncio
import time

# Do'stlarning telefon raqamlari
raqamlar = ["+998901234567", "+998909876543", "+998931234567"]

# Asinxron SMS yuborishni taqlid qiluvchi funksiya
async def sms_yubor_asinxron(raqam):
    print(f"{raqam} raqamiga SMS yuborilmoqda...")
    await asyncio.sleep(2)  # SMS yuborishni taqlid qilish
    print(f"{raqam} raqamiga SMS yuborildi.")

# Asinxron SMS yuborish funksiyasi
async def asinxron_sms_yuborish():
    tasks = [sms_yubor_asinxron(raqam) for raqam in raqamlar]
    await asyncio.gather(*tasks)

# Asinxron kodni ishga tushirish
start = time.time()
asyncio.run(asinxron_sms_yuborish())
end = time.time()
print(f"Asinxron usulda bajarildi: {end - start:.2f} soniya")
