import time

def ish_vaqti(nom):
    print(f"{nom} boshlangan...")
    time.sleep(2)
    print(f"{nom} tugadi!")

def asosiy():
    ish_vaqti("1-vazifa")
    ish_vaqti("2-vazifa")
    ish_vaqti("3-vazifa")

if __name__ == "__main__":
    boshlanish = time.time()
    asosiy()
    tugash = time.time()
    print(f"Umumiy vaqt: {tugash - boshlanish:.2f} soniya")
