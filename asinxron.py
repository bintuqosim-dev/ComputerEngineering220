import asyncio
import time


async def say_hello():
    await asyncio.sleep(2)
    print("Salom")

async def main():
    start_time = time.time()


    await asyncio.gather(say_hello(), say_hello(), say_hello())
    print(f"Asinxron bajarildi: {time.time() - start_time:.2f} soniya")


asyncio.run(main())
