# utils/timer.py

import time

class Timer:
    results = []

    @staticmethod
    def time_function(func, description, *args):
        start_time = time.time()
        result = func(*args)
        elapsed_time = time.time() - start_time
        Timer.results.append((description, elapsed_time))
        print(f"{description}: {elapsed_time:.4f} seconds")
        return result
