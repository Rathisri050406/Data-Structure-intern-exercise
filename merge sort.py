# Merge two sorted sublists
def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Recursive merge sort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

# Main program
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid number of elements. Must be greater than 0.")
else:
    arr = []
    print("Enter the elements:")
    for i in range(n):
        num = int(input(f"Element {i+1}: "))
        arr.append(num)

    sorted_arr = merge_sort(arr)

    print("\nOriginal array:", arr)
    print("Sorted array:", sorted_arr)
