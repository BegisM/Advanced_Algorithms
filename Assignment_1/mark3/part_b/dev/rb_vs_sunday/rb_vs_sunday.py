import random
import time

import plotly.graph_objects as go

from Assignment_1.mark3.part_b.dev import rabin_karp, sunday
from Assignment_1.mark3.part_b.dev.rb_vs_sunday.text_gen import generate_rabin_karp_test_text

attempts = 0
while True:
    # Create a long random text
    random.seed(42)  # For reproducibility
    """
    text = ''.join(random.choices(string.ascii_lowercase, k=10000000)) + "pattern"
    with open("example/rb_beats_sunday_input.txt", "r") as file:
        text = file.read()
        
    # Pattern that is short and unique
    pattern = "pattern"
    """
    # Example usage:
    pattern_length = 10
    text_length = 2000
    pattern_frequency = 50
    text, pattern = generate_rabin_karp_test_text(pattern_length, text_length, pattern_frequency)

    # Measure execution time for Rabin-Karp
    start_time = time.time()
    rabin_karp_results = rabin_karp.rabin_karp(text, pattern)
    rabin_karp_time = time.time() - start_time

    # Measure execution time for Sunday
    start_time = time.time()
    sunday_results = sunday.sunday(text, pattern)
    sunday_time = time.time() - start_time

    faster_value = sunday_time / rabin_karp_time
    print(f"Rabin-Karp execution time: {rabin_karp_time} seconds")
    print(f"Sunday execution time: {sunday_time} seconds")
    print(f"Rabin-Karp found pattern at indices: {rabin_karp_results}")
    print(f"Sunday found pattern at indices: {sunday_results}")
    print(f"Rabin-Karp is {faster_value} times faster than Sunday in this case")
    print("*" * 20)

    if faster_value > 2:
        print("There was needed {} attempts to find a case where Rabin-Karp is faster than Sunday".format(attempts))
        # Create bar charts
        fig = go.Figure(data=[
            go.Bar(name='Rabin-Karp', x=['Rabin-Karp'], y=[rabin_karp_time]),
            go.Bar(name='Sunday', x=['Sunday'], y=[sunday_time])
        ])

        # Update the layout
        fig.update_layout(
            title='Execution Time Comparison',
            xaxis_title='Algorithm',
            yaxis_title='Execution Time (seconds)',
            barmode='group'
        )

        with open("rb_beats_sunday.html", "w") as file:
            file.write(fig.to_html())

        print(text)
        with open("rb_beats_sunday_text.txt", "w") as file:
            file.write(text)

        break

    attempts += 1
