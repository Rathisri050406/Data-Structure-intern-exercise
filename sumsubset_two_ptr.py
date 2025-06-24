# Getting input from the user
n = int(input("Enter number of elements: "))

if n <= 0:
    print("Invalid number of elements.")
else:
    arr = []
    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input(f"Element {i+1}: ")))

    target = int(input("Enter the target sum: "))

    if target < 0:
        print("Invalid target number.")
    else:
        arr.sort()
        i = 0
        j = len(arr) - 1
        pairs = []

        while i < j:
            current_sum = arr[i] + arr[j]
            if current_sum == target:
                pairs.append((arr[i], arr[j]))

                # Skip duplicates
                current_i = arr[i]
                current_j = arr[j]
                while i < j and arr[i] == current_i:
                    i += 1
                while i < j and arr[j] == current_j:
                    j -= 1

            elif current_sum < target:
                i += 1
            else:
                j -= 1

        if not pairs:
            print("No pair found.")
        else:
            print("Pairs that sum to", target, "are:")
            for x, y in pairs:
                print(f"{x} + {y} = {target}")
