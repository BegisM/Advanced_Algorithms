import random
import string
import time


def measure_time(algorithm, text, pattern):
    start_time = time.time()
    algorithm(text, pattern)
    end_time = time.time()
    return end_time - start_time


def generate_text(length):
    return ''.join(random.choices(string.ascii_letters + ' ', k=length))


def run_experiments(algorithms, text_lengths, pattern):
    results = {name: [] for name, _ in algorithms}

    for length in text_lengths:
        text = generate_text(length)
        for name, algorithm in algorithms:
            times = measure_time(algorithm, text, pattern)
            results[name].append(times)

    return results


