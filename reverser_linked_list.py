# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a linked list based on yes/no inputs
def create_linked_list_dynamic():
    head = None
    current = None

    while True:
        response = input("Do you want to add a node? (yes/no): ").strip().lower()
        if response != 'yes':
            break

        val = int(input("Enter node value: "))
        new_node = Node(val)

        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node

    return head

# Function to print a linked list
def print_linked_list(head):
    if not head:
        print("Linked list is empty.")
        return

    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev  # New head

# --------- MAIN PROGRAM ---------
print("Create your linked list:")
head = create_linked_list_dynamic()

print("\nOriginal Linked List:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)

print("\nReversed Linked List:")
print_linked_list(reversed_head)
