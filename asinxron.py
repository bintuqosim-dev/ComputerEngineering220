import asyncio
import time

async def ish_vaqti(nom):
    print(f"{nom} boshlangan...")
    await asyncio.sleep(2)
    print(f"{nom} tugadi!")

async def asosiy():

    vazifalar = [ish_vaqti("1-vazifa"), ish_vaqti("2-vazifa"), ish_vaqti("3-vazifa")]
    await asyncio.gather(*vazifalar)

if __name__ == "__main__":
    boshlanish = time.time()
    asyncio.run(asosiy())
    tugash = time.time()
    print(f"Barcha vazifalar bajarildi! Umumiy vaqt: {tugash - boshlanish:.2f} soniya")
