Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import threading
... import time
... 
... def birinchi_thread():
...     for i in range(1, 11):
...         print(f"Birinchi thread soni: {i}")
...         time.sleep(0.5)  
... 
... def ikkinchi_thread():
...     for i in range(1, 11):
...         print("Ikkinchi thread: Thread tugadi!")
...         time.sleep(0.5)
... 
... thread1 = threading.Thread(target=birinchi_thread)
... thread2 = threading.Thread(target=ikkinchi_thread)
... 
... thread1.start()
... thread2.start()
... 
... thread1.join()
... thread2.join()
... 
... print("Barcha threadlar tugadi!")
