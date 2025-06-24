
# Node class for storing student data
class Node:
    def __init__(self, name, rollno, mark1, mark2, mark3):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = mark1 + mark2 + mark3
        self.next = None

# Function to add student node at the end
def add_student_node(head, name, rollno, mark1, mark2, mark3):
    new_node = Node(name, rollno, mark1, mark2, mark3)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Function to create the linked list by user input
def create_student_list():
    head = None
    while True:
        print("\nEnter student details:")
        name = input("Name: ")
        rollno = int(input("Roll Number: "))
        mark1 = int(input("Mark 1: "))
        mark2 = int(input("Mark 2: "))
        mark3 = int(input("Mark 3: "))

        head = add_student_node(head, name, rollno, mark1, mark2, mark3)

        more = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    return head

# Function to print all student records
def print_student_list(head):
    print("\nStudent Records:")
    current = head
    while current:
        print(f"Name: {current.name}, Roll No: {current.rollno}, "
              f"Marks: [{current.mark1}, {current.mark2}, {current.mark3}], "
              f"Total: {current.total}")
        current = current.next

# Main program
head = create_student_list()
print_student_list(head)
