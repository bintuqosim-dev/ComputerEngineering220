import time
import random

def get_temperature(sensor_id):
    time.sleep(1)  # Sensor ma'lumotini olish uchun vaqt
    temperature = random.uniform(20.0, 30.0)  # Tasodifiy harorat
    print(f"Sensor {sensor_id}: {temperature:.2f}°C")
    return temperature

def main_sync():
    start_time = time.perf_counter()  # Vaqtni o'lchashni boshlash
    sensors = range(1, 11)  # 10 ta sensor
    temperatures = [get_temperature(sensor) for sensor in sensors]
    avg_temperature = sum(temperatures) / len(temperatures)
    end_time = time.perf_counter()  # Vaqtni o'lchashni yakunlash
    print(f"O'rtacha harorat: {avg_temperature:.2f}°C")
    print(f"Sinxron dastur sarflagan vaqt: {end_time - start_time:.2f} soniya")

if __name__== "__main__":
    print("Sinxron dastur:")
    main_sync()