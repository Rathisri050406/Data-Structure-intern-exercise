def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(str(val) for val in row))


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix_2d = []
    print("Enter the elements row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Element at row {i+1}, column {j+1}: "))
            row.append(val)
        matrix_2d.append(row)

    print_matrix(matrix_2d, "Original Matrix")

    # Rotate 90 degrees clockwise: transpose + reverse rows
    rotated_matrix = []
    for i in range(cols):
        row = []
        for j in range(rows - 1, -1, -1):
            row.append(matrix_2d[j][i])
        rotated_matrix.append(row)

    print_matrix(rotated_matrix, "Rotated Matrix (90 degrees clockwise)")

if __name__ == "__main__":
    main()
