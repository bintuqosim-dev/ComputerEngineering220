import time

def say_hello():
    time.sleep(2)
    print("Salom")

start_time = time.time()

say_hello()
say_hello()
say_hello()

print(f"Sinxron bajarildi: {time.time() - start_time:.2f} soniya")
