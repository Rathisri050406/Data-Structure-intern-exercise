def get_array_input(n, label):
    arr = []
    print(f"Enter {n} elements for {label} array:")
    for i in range(n):
        num = int(input(f"Element {i+1}: "))
        arr.append(num)
    return arr

def find_largest_common_element(arr1, arr2):
    # Sort both arrays in ascending order
    arr1.sort()
    arr2.sort()

    # Start from the end to find largest common element
    pointer1 = len(arr1) - 1
    pointer2 = len(arr2) - 1

    while pointer1 >= 0 and pointer2 >= 0:
        if arr1[pointer1] == arr2[pointer2]:
            return arr1[pointer1]
        elif arr1[pointer1] > arr2[pointer2]:
            pointer1 -= 1
        else:
            pointer2 -= 1
    return None

# Main input
num1 = int(input("Enter number of elements in first array: "))
arr1 = get_array_input(num1, "first")

num2 = int(input("Enter number of elements in second array: "))
arr2 = get_array_input(num2, "second")

# Find and display the result
common_element = find_largest_common_element(arr1, arr2)
if common_element is not None:
    print("Largest common element is:", common_element)
else:
    print("No common element found.")
