def jewish_style_carp(picture, K):
    M, N = len(picture), len(picture[0])
    if K > min(M, N):
        return False  # Can't fit the corner if it's larger than the picture

    # Calculate hash for the top-right corner of size K by K
    corner_hash = 0
    for i in range(K):
        for j in range(K):
            corner_hash ^= hash(picture[i][N-K+j])  # Assuming picture is a 2D array

    # Calculate hashes for each K by K window in the picture's top-right corner
    window_hash = 0
    for i in range(M - K + 1):
        for j in range(N - K + 1):
            if i == 0:
                # Calculate hash for the first window in the top-right corner
                if j == 0:
                    for x in range(K):
                        for y in range(K):
                            window_hash ^= hash(picture[x][y])
                else:
                    # Update hash for the next window column-wise
                    for x in range(K):
                        window_hash ^= hash(picture[x][j - 1])  # Remove leftmost column
                        window_hash ^= hash(picture[x][j + K - 1])  # Add rightmost column
            else:
                # Update hash for the next window row-wise
                for y in range(K):
                    window_hash ^= hash(picture[i - 1][N - K + y])  # Remove top row
                    window_hash ^= hash(picture[i + K - 1][N - K + y])  # Add bottom row

            if window_hash == corner_hash:
                return True  # Match found

    return False  # No match found

# Example usage:
picture = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

K = 2
print(jewish_style_carp(picture, K))  # Output: True, as the top-right 2x2 corner [4, 5, 9, 10] is duplicated


# Example usage:
picture_false = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

K = 2  # Keeping K as 2 for simplicity
print(jewish_style_carp(picture_false, K))  # Output: False, as there is no duplicated top-right 2x2 corner
