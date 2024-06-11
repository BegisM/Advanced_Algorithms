def compute_initial_hash(matrix, row, col, K, base=256, prime=101):
    """ Compute hash for the KxK sub-matrix starting at (row, col) """
    hash_val = 0
    for i in range(K):
        for j in range(K):
            hash_val = (hash_val * base + matrix[row + i][col + j]) % prime
    return hash_val


def update_hash(hash_val, matrix, old_row, old_col, new_row, new_col, K, vertical, base=256, prime=101):
    """ Update hash value when sliding window """
    if vertical:
        for j in range(K):
            # Remove the old row and add the new row
            hash_val = (hash_val - matrix[old_row][old_col + j] * pow(base, K - 1, prime)) % prime
            hash_val = (hash_val * base + matrix[new_row][new_col + j]) % prime
    else:
        for i in range(K):
            # Remove the old column and add the new column
            hash_val = (hash_val - matrix[old_row + i][old_col] * pow(base, K - 1, prime)) % prime
            hash_val = (hash_val * base + matrix[new_row + i][new_col]) % prime
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

    prime = 101  # A prime number for the hash function
    base = 256  # Base for the hash function

    pattern_hash = compute_initial_hash(matrix, 0, N - K, K, base, prime)

    # Set to store the hash values of sub-matrices encountered
    hash_values = set()

    # Compute initial hash values for the first row of sub-matrices
    hash_values_row = [compute_initial_hash(matrix, i, 0, K, base, prime) for i in range(M - K + 1)]

    # Check each sub-matrix in the matrix
    for j in range(N - K + 1):
        current_hash = hash_values_row[0]
        for i in range(M - K + 1):
            if current_hash in hash_values:
                return True  # Found a duplicate sub-matrix
            hash_values.add(current_hash)

            # Update hash value for the next row
            if i < M - K:
                current_hash = update_hash(current_hash, matrix, i, j, i + 1, j, K, vertical=False, base=base, prime=prime)

        # Update hash values for the next column of sub-matrices
        if j < N - K:
            for i in range(M - K + 1):
                hash_values_row[i] = update_hash(hash_values_row[i], matrix, i, j, i, j + 1, K, vertical=True, base=base, prime=prime)

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

