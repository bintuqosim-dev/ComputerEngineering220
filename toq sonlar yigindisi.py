class Element:
    def __init__(self, value):
        self.value = value

def sum_of_odd_numbers(elements):
    total_sum = 0
    for elem in elements:
        if elem.value % 2 != 0:
            total_sum += elem.value
    return total_sum

n = int(input("Massivdagi elementlar sonini kiriting: "))

elements = []

for i in range(n):
    value = int(input(f"Massivning {i + 1}-elementining qiymatini kiriting: "))
    elements.append(Element(value))

result = sum_of_odd_numbers(elements)

print("Massivdagi toq sonlar yig'indisi:", result)
