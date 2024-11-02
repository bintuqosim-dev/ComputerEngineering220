class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)
        print(f"{item} stekga qo'shildi.")


    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} stekdan olindi.")
            return item
        else:
            print("Stek bo'sh!")


    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stek bo'sh!")


    def is_empty(self):
        return len(self.stack) == 0


    def display(self):
        print("Stack:", self.stack)


stack = Stack()


stack.push(5)
stack.push(4)
stack.push(1)
stack.display()

print("Oxirgi element:", stack.peek())
stack.pop()
stack.display()
print("Stack bo'shmi?", stack.is_empty())
