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

# Function to insert a student at the beginning
def insert_student_at_beginning(head, name, rollno, mark1, mark2, mark3):
    new_node = Node(name, rollno, mark1, mark2, mark3)
    new_node.next = head  # Point to current head
    head = new_node       # New node becomes the new head
    print(f"Inserted {name} at the beginning.")
    return head

# Function to print all student records
def print_student_list(head):
    if not head:
        print("\nNo student records to display.")
        return

    print("\nStudent Records:")
    current = head
    while current:
        print(f"Name: {current.name}, Roll No: {current.rollno}, "
              f"Marks: [{current.mark1}, {current.mark2}, {current.mark3}], "
              f"Total: {current.total}")
        current = current.next

# Function to create student list by inserting at the beginning
def create_student_list():
    head = None
    while True:
        print("\nEnter student details to insert at beginning:")
        name = input("Name: ")
        rollno = int(input("Roll Number: "))
        mark1 = int(input("Mark 1: "))
        mark2 = int(input("Mark 2: "))
        mark3 = int(input("Mark 3: "))

        head = insert_student_at_beginning(head, name, rollno, mark1, mark2, mark3)

        more = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    return head

# Main program
if __name__ == "__main__":
    head = create_student_list()
    print_student_list(head)
