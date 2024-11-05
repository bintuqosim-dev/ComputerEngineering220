def is_kabisa_yili(yil):
    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)


yil = int(input("Yilni kiriting: "))
print(f"{yil} kabisa yili." if is_kabisa_yili(yil) else f"{yil} kabisa yili emas.")

