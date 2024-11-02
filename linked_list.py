# 1-misol

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()

# 2-misol
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#         new_node.prev = last_node
#
#     def print_list(self):
#         cur_node = self.head
#         while cur_node:
#             print(cur_node.data, end=" <-> ")
#             cur_node = cur_node.next
#         print("None")
#
#
# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.print_list()
#
