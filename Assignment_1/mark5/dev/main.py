def hash_matrix(matrix, mod=2 ** 61 - 1):
    """ Hash a KxK matrix using base hashing and bitwise operations. """
    K = len(matrix)
    hash_val = 0
    for row in matrix:
        for value in row:
            # Use a large prime base for polynomial rolling hash
            hash_val = (hash_val * 257 & mod) ^ value
    return hash_val


def rabin_karp_2d(image, K):
    M = len(image)
    N = len(image[0])

    # Edge case where the submatrix size is larger than the image dimensions
    if K > M or K > N:
        return False

    # Compute the hash for the top-right KxK corner
    top_right_corner = [image[i][N - K:N] for i in range(K)]
    target_hash = hash_matrix(top_right_corner)

    # Initialize a set to store unique hashes, except the top-right corner hash
    seen_hashes = set()

    # Iterate over each possible KxK submatrix in the image
    for start_row in range(M - K + 1):
        for start_col in range(N - K + 1):
            # Extract the KxK submatrix
            submatrix = [image[i][start_col:start_col + K] for i in range(start_row, start_row + K)]
            submatrix_hash = hash_matrix(submatrix)

            # Check if this submatrix is the top-right corner
            if start_row == 0 and start_col == N - K:
                continue  # Skip the comparison for the top-right corner itself

            # Check for hash collision
            if submatrix_hash == target_hash:
                return True

            # Store hash in set for debugging or further checks
            seen_hashes.add(submatrix_hash)

    return False


if __name__ == '__main__':
    # Example usage with a dummy image
    image = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 4, 5, 6, 7, 8],
        [29, 30, 31, 12, 13, 14, 15, 16],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 20, 21, 22, 23, 24],
        [45, 46, 47, 48, 49, 50, 51, 52]
    ]
    K = 2
    found_duplicate = rabin_karp_2d(image, K)
    print("Duplicate found:", found_duplicate)
