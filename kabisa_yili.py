def is_kabisa_yili(yil):
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        return True
    else:
        return False


yil = int(input("Yilni kiriting: "))
if is_kabisa_yili(yil):
    print(f"{yil} kabisa yili.")
else:
    print(f"{yil} kabisa yili emas.")
