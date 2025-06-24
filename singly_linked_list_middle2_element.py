
# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Method to add a node to the linked list
def add_node(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Function to find the middle of the linked list
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

# Main program
head = None
while True:
    val = int(input("Enter a node value: "))
    head = add_node(head, val)
    
    more = input("Do you want to add another node? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Display the linked list
print("\nLinked List:")
print_linked_list(head)

# Find and print the middle element
middle = find_middle(head)
print(f"\nMiddle element is: {middle}")
