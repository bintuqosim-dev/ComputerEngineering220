import aiofiles
import asyncio

async def read_file_async():
    async with aiofiles.open("file.txt", "r") as file:
        data = await file.read()
    print("Fayldagi ma'lumot:", data)

asyncio.run(read_file_async())
