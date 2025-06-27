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

# Function to insert a student at a specific position
def insert_student_at_position(head, pos, name, rollno, mark1, mark2, mark3):
    new_node = Node(name, rollno, mark1, mark2, mark3)

    if pos == 0:
        new_node.next = head
        head = new_node
        print(f"Inserted {name} at position {pos}")
        return head

    current = head
    count = 0

    # Traverse to node before desired position
    while current is not None and count < pos - 1:
        current = current.next
        count += 1

    if current is None:
        print("Invalid position.")
        return head

    new_node.next = current.next
    current.next = new_node
    print(f"Inserted {name} at position {pos}")
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

# Function to create student list with insert at position
def create_student_list():
    head = None
    while True:
        print("\nEnter student details:")
        name = input("Name: ")
        rollno = int(input("Roll Number: "))
        mark1 = int(input("Mark 1: "))
        mark2 = int(input("Mark 2: "))
        mark3 = int(input("Mark 3: "))

        pos = int(input("Enter the position to insert (starting at 0): "))
        if pos < 0:
            print("Invalid position. Must be 0 or more.")
        else:
            head = insert_student_at_position(head, pos, name, rollno, mark1, mark2, mark3)

        more = input("Do you want to add another student? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    return head

# Main program
if __name__ == "__main__":
    head = create_student_list()
    print_student_list(head)
