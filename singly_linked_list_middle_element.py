# Node class to represent each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Get number of nodes from the user
node_count = int(input("Enter the number of nodes: "))

# Create the head node
num = int(input("Enter node 1: "))
head = Node(num)
current = head

# Create the remaining nodes
for index in range(2, node_count + 1):
    next_num = int(input(f"Enter node {index}: "))
    new_node = Node(next_num)
    current.next = new_node
    current = new_node

# Print the original linked list
print("\nOriginal Linked List:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Find the middle element using two-pointer technique
slow_pointer = head
fast_pointer = head

while fast_pointer and fast_pointer.next:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next

# Print the middle node data
print("\nMiddle element is:", slow_pointer.data)
