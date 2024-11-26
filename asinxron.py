import asyncio
import random
import time

async def get_temperature_async(sensor_id):
    await asyncio.sleep(1)  # Sensor ma'lumotini olish uchun vaqt
    temperature = random.uniform(20.0, 30.0)  # Tasodifiy harorat
    print(f"Sensor {sensor_id}: {temperature:.2f}°C")
    return temperature

async def main_async():
    start_time = time.perf_counter()  # Vaqtni o'lchashni boshlash
    sensors = range(1, 11)  # 10 ta sensor
    tasks = [get_temperature_async(sensor) for sensor in sensors]
    temperatures = await asyncio.gather(*tasks)
    avg_temperature = sum(temperatures) / len(temperatures)
    end_time = time.perf_counter()  # Vaqtni o'lchashni yakunlash
    print(f"O'rtacha harorat: {avg_temperature:.2f}°C")
    print(f"Asinxron dastur sarflagan vaqt: {end_time - start_time:.2f} soniya")

if __name__ == "__main__":
    print("Asinxron dastur:")
    asyncio.run(main_async())