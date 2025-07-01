# main.py

from phonebook import PhoneBook

def menu():
    pb = PhoneBook()

    while True:
        print("\n=== Phone Book Menu ===")
        print("1. Insert at Start")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Print Phone Book")
        print("5. Reverse Phone Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            pb.insert_at_start(name, phone)

        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            pb.insert_at_end(name, phone)

        elif choice == "3":
            try:
                pos = int(input("Enter position: "))
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                pb.insert_at_position(name, phone, pos)
            except ValueError:
                print("Position must be a number.")

        elif choice == "4":
            pb.print_list()

        elif choice == "5":
            pb.reverse_list()

        elif choice == "6":
            print("Exiting Phone Book.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    menu()
