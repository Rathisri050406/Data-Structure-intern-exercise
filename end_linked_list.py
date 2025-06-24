# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to add node at end
def add_node(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Function to create linked list with yes/no option
def create_linked_list():
    head = None
    while True:
        val = int(input("Enter node value: "))
        head = add_node(head, val)
        more = input("Do you want to add another node? (yes/no): ").strip().lower()
        if more != "yes":
            break
    return head

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Function to find the Nth node from the end
def find_nth_from_end(head, N):
    fast = head
    slow = head

    for _ in range(N):
        if not fast:
            return -1
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.data if slow else -1

# ---------------- Main Program ----------------

# Create linked list
head = create_linked_list()

# Print linked list
print("\nLinked List:")
print_linked_list(head)

# Input N
N = int(input("\nEnter the value of N (from end): "))

# Find and print Nth node from end
result = find_nth_from_end(head, N)
print(f"\n{N}th node from the end is: {result}")
