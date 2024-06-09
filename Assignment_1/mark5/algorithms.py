def compute_initial_hash(matrix, row, col, K):
    """ Compute hash for the KxK sub-matrix starting at (row, col) """
    hash_val = 0
    for i in range(row, row + K):
        for j in range(col, col + K):
            hash_val ^= hash(matrix[i][j])
    return hash_val


def update_hash(hash_val, matrix, old_row, old_col, new_row, new_col, K, vertical):
    """ Update hash value when sliding window """
    if vertical:
        for j in range(K):
            hash_val ^= hash(matrix[old_row][old_col + j])
            hash_val ^= hash(matrix[new_row][new_col + j])
    else:
        for i in range(K):
            hash_val ^= hash(matrix[old_row + i][old_col])
            hash_val ^= hash(matrix[new_row + i][new_col])
    return hash_val


def is_submatrix_equal(matrix, row1, col1, row2, col2, K):
    """ Check if KxK sub-matrix at (row1, col1) is equal to KxK sub-matrix at (row2, col2) """
    for i in range(K):
        for j in range(K):
            if matrix[row1 + i][col1 + j] != matrix[row2 + i][col2 + j]:
                return False
    return True


def rabin_karp_2d(matrix, K):
    M, N = len(matrix), len(matrix[0])
    if K > M or K > N:
        return False

    pattern_hash = compute_initial_hash(matrix, 0, N - K, K)
    current_hash = 0
    for i in range(M - K + 1):
        if i == 0:
            current_hash = compute_initial_hash(matrix, i, 0, K)
        else:
            current_hash = update_hash(current_hash, matrix, i - 1, 0, i + K - 1, 0, K, vertical=True)

        if current_hash == pattern_hash and is_submatrix_equal(matrix, i, 0, 0, N - K, K):
            return True

        for j in range(1, N - K + 1):
            current_hash = update_hash(current_hash, matrix, i, j - 1, i, j + K - 1, K, vertical=False)

            if current_hash == pattern_hash and is_submatrix_equal(matrix, i, j, 0, N - K, K):
                return True

    return False


# Example usage:

# True case
picture_true = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 4, 5],  # Top-right 2x2 corner [4, 5] is duplicated here
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

K = 2
print(rabin_karp_2d(picture_true, K))  # Output: True

# False case
picture_false = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],  # No duplication of top-right 2x2 corner
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

print(rabin_karp_2d(picture_false, K))  # Output: False

