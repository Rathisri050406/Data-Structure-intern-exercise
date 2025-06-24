def remove_duplicates_from_sorted(arr):
    if not arr:
        return []

    unique = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique.append(arr[i])
    return unique

# Main program
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid or empty input.")
else:
    arr = []
    print("Enter the elements (in sorted order):")
    for i in range(n):
        num = int(input(f"Element {i+1}: "))
        arr.append(num)

    # Uncomment the line below if input may not be sorted
    # arr.sort()

    result = remove_duplicates_from_sorted(arr)
    print("\nOriginal array:", arr)
    print("Array after removing duplicates:", result)
