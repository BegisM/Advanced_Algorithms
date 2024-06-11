import matplotlib.pyplot as plt
import numpy as np
import time

from Assignment_1.mark5.dev.main import rabin_karp_2d


def hash_matrix(matrix, mod=2 ** 61 - 1):
    """ Hash a KxK matrix using base hashing and bitwise operations. """
    K = len(matrix)
    hash_val = 0
    for row in matrix:
        for value in row:
            hash_val = (hash_val * 257 & mod) ^ value
    return hash_val


# Parameters
image_sizes = [10, 50, 100, 200, 300, 400, 500]  # Varying image sizes (NxN)
K = 3  # Sub-region size
times = []

# Generate test images and measure runtime
for size in image_sizes:
    # Create a random image of given size
    image = np.random.randint(0, 256, (size, size)).tolist()
    start_time = time.time()
    rabin_karp_2d(image, K)
    end_time = time.time()
    times.append(end_time - start_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(image_sizes, times, marker='o', linestyle='-', color='b')
plt.title('Performance of Rabin-Karp 2D Algorithm')
plt.xlabel('Image Size (NxN)')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()
