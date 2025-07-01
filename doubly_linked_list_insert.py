class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        print(f"{data} inserted at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"{data} inserted as the first node (end).")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"{data} inserted at the end.")

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position!")
            return
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 2):
            if not temp:
                print("Position out of range.")
                return
            temp = temp.next
        if not temp:
            print("Position out of range.")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        print(f"{data} inserted at position {position}.")

    def print_forward(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        print("Doubly Linked List (forward):", end=" ")
        while temp:
            print(temp.data, end=" <=> " if temp.next else "")
            temp = temp.next
        print()

# Menu-driven program
def menu():
    dll = DoublyLinkedList()
    while True:
        print("\n--- Doubly Linked List Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Display List")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter data to insert at beginning: ")
            dll.insert_at_beginning(data)

        elif choice == "2":
            data = input("Enter data to insert at end: ")
            dll.insert_at_end(data)

        elif choice == "3":
            data = input("Enter data to insert: ")
            try:
                pos = int(input("Enter position to insert at: "))
                dll.insert_at_position(data, pos)
            except ValueError:
                print("Invalid position! Enter a number.")

        elif choice == "4":
            dll.print_forward()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
