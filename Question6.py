# A program to represent a sparse using arrays
def to_sparse_triplet(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Header row: [total_rows, total_cols, count_of_non_zero]
    triplet = [[rows, cols, 0]]
    non_zero_count = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                triplet.append([r, c, matrix[r][c]])
                non_zero_count += 1

    triplet[0][2] = non_zero_count
    return triplet

# Example 4x5 Sparse Matrix
sparse_matrix = [
    [0, 0, 3, 0, 4],
    [0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 6, 0, 0]
]

triplet_representation = to_sparse_triplet(sparse_matrix)

print("Row\tCol\tValue")
for row in triplet_representation:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")