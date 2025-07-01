# phonebook.py

class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class PhoneBook:
    def __init__(self):
        self.head = None

    def insert_at_start(self, name, phone):
        new_node = Node(name, phone)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, name, phone):
        new_node = Node(name, phone)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, name, phone, pos):
        if pos <= 0:
            print("Invalid position!")
            return
        if pos == 1:
            self.insert_at_start(name, phone)
            return
        new_node = Node(name, phone)
        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position!")
            return
        new_node.next = temp.next
        temp.next = new_node

    def print_list(self):
        if not self.head:
            print("Phone book is empty.")
            return
        print("\n--- Phone Book ---")
        temp = self.head
        while temp:
            print(f"Name: {temp.name} | Phone: {temp.phone}")
            temp = temp.next

    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        print("Phone book reversed successfully.")
