import time
import random
import string
import plotly.graph_objects as go

# Rabin-Karp Algorithm
def rabin_karp(text, pattern):
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    m = len(pattern)
    n = len(text)
    h = 1
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    results = []

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        if p == t:
            # Check for characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                results.append(i)

        # Calculate hash value for next window of text
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q

    return results

# Sunday Algorithm
def sunday(text, pattern):
    m = len(pattern)
    n = len(text)
    results = []

    # Create shift table
    shift = {c: m + 1 for c in text}
    for i in range(m):
        shift[pattern[i]] = m - i

    i = 0
    while i <= n - m:
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            results.append(i)

        if i + m < n:
            i += shift.get(text[i + m], m + 1)
        else:
            break

    return results

import plotly.graph_objects as go

while True:
    # Create a long random text
    random.seed(42)  # For reproducibility
    # text = ''.join(random.choices(string.ascii_lowercase, k=100000)) + "pattern"

    with open("example/rb_beats_sunday_input.txt", "r") as file:
        text = file.read()

    # Pattern that is short and unique
    pattern = "pattern"

    # Measure execution time for Rabin-Karp
    start_time = time.time()
    rabin_karp_results = rabin_karp(text, pattern)
    rabin_karp_time = time.time() - start_time

    # Measure execution time for Sunday
    start_time = time.time()
    sunday_results = sunday(text, pattern)
    sunday_time = time.time() - start_time

    faster_value = sunday_time / rabin_karp_time
    print(f"Rabin-Karp execution time: {rabin_karp_time} seconds")
    print(f"Sunday execution time: {sunday_time} seconds")
    print(f"Rabin-Karp found pattern at indices: {rabin_karp_results}")
    print(f"Sunday found pattern at indices: {sunday_results}")
    print(f"Rabin-Karp is {faster_value} times faster than Sunday in this case")
    print("*" * 20)

    if faster_value > 2:
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
