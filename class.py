class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        # Stack bo'sh yoki yo'qligini tekshirish
        return len(self.stack) == 0

    def push(self, item):
        # Element qo'shish
        self.stack.append(item)
        print(f"{item} qo'shildi")

    def pop(self):
        # Oxirgi elementni olib tashlash
        if self.is_empty():
            return "Stack bo'sh"
        return self.stack.pop()

    def peek(self):
        # Oxirgi elementni ko'rish
        if self.is_empty():
            return "Stack bo'sh"
        return self.stack[-1]

    def size(self):
        # Stackdagi elementlar soni
        return len(self.stack)

# Stack obyekti yaratish
my_stack = Stack()

# Stack operatsiyalarini bajarish
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Stackning yuqorigi elementi:", my_stack.peek())
print("Olingan element:", my_stack.pop())
print("Stackdagi elementlar soni:", my_stack.size())
print("Stack hozirda bo'shmi?:", my_stack.is_empty())
