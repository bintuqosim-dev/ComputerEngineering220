# import numpy as np
#
# # Massivni tuzish
# massiv = np.array([3, 7, 9, 2, 6])
#
# # o'rta arifmetigi
# orta_arifmetik = np.mean(massiv)
#
# # O'rta arifmetigiga yagin bo'lgan elementning tartib ragami
# indeks = np. argmin(np.abs(massiv - orta_arifmetik))
#
# print ("O'rta arifmetigiga yagin bo'lgan element taptib ragami:", indeks)

import numpy as np

# Massiv elementlarini kiritish
elementlar = input("Massiv elementlarini vergul orqali kiriting (masalan: 3, 7, 9, 2, 6): ")
massiv = np.array([int(x) for x in elementlar.split(",")])

# O'rta arifmetigini hisoblash
orta_arifmetik = np.mean(massiv)

# O'rta arifmetikga eng yaqin bo'lgan elementning tartib raqamini topish
indeks = np.argmin(np.abs(massiv - orta_arifmetik))

print("O'rta arifmetikga eng yaqin bo'lgan element tartib raqami:", indeks)
