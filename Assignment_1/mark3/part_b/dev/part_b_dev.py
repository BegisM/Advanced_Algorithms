import time
import random
import string
from pathlib import Path

import plotly.graph_objects as go


def generate_text(length):
    return ''.join(random.choices(string.ascii_lowercase + string.whitespace, k=length))


def generate_pattern(length):
    return ''.join(random.choices(string.ascii_lowercase + string.whitespace, k=length))


# Sunday algorithm
def sunday_search(text, pattern):
    m, n = len(pattern), len(text)
    if m > n: return -1
    shift = {pattern[i]: m - i for i in range(m)}
    i = 0
    while i <= n - m:
        if text[i:i + m] == pattern:
            return i
        i += shift.get(text[i + m], m)
    return -1


# Gusfield Z algorithm
def gusfield_z_search(text, pattern):
    concat = pattern + "$" + text
    Z = [0] * len(concat)
    l, r, K = 0, 0, 0
    for i in range(1, len(concat)):
        if i > r:
            l, r = i, i
            while r < len(concat) and concat[r] == concat[r - l]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            K = i - l
            if Z[K] < r - i + 1:
                Z[i] = Z[K]
            else:
                l = i
                while r < len(concat) and concat[r] == concat[r - l]:
                    r += 1
                Z[i] = r - l
                r -= 1
    for i in range(len(Z)):
        if Z[i] == len(pattern):
            return i - len(pattern) - 1
    return -1


# Knuth-Morris-Pratt algorithm
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


# Rabin-Karp algorithm
def rabin_karp_search(text, pattern, q=101):
    d = 256
    m, n = len(pattern), len(text)
    p, t, h = 0, 0, 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1


# Performance measurement
def measure_performance(text, pattern, search_func):
    start_time = time.time()
    search_func(text, pattern)
    return time.time() - start_time


# Generate text and patterns
text_length = 100000
pattern_length = 50

text = generate_text(text_length)
pattern_sunday_vs_gusfield = generate_pattern(pattern_length)
pattern_kmp_vs_rk = generate_pattern(pattern_length)
pattern_rk_vs_sunday = generate_pattern(pattern_length)

# Measure performance
time_sunday = measure_performance(text, pattern_sunday_vs_gusfield, sunday_search)
time_gusfield = measure_performance(text, pattern_sunday_vs_gusfield, gusfield_z_search)

time_kmp = measure_performance(text, pattern_kmp_vs_rk, kmp_search)
time_rk = measure_performance(text, pattern_kmp_vs_rk, rabin_karp_search)

time_rk_again = measure_performance(text, pattern_rk_vs_sunday, rabin_karp_search)
time_sunday_again = measure_performance(text, pattern_rk_vs_sunday, sunday_search)

# Plot results
fig = go.Figure()

fig.add_trace(go.Bar(
    x=['Sunday', 'Gusfield Z'],
    y=[time_sunday, time_gusfield],
    name='Sunday vs Gusfield Z',
    marker_color='blue'
))

fig.add_trace(go.Bar(
    x=['KMP', 'Rabin-Karp'],
    y=[time_kmp, time_rk],
    name='KMP vs Rabin-Karp',
    marker_color='orange'
))

fig.add_trace(go.Bar(
    x=['Rabin-Karp', 'Sunday'],
    y=[time_rk_again, time_sunday_again],
    name='Rabin-Karp vs Sunday',
    marker_color='green'
))

fig.update_layout(
    title='Algorithm Performance Comparison',
    xaxis=dict(title='Algorithms'),
    yaxis=dict(title='Time (seconds)'),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

current_file = Path(__file__).resolve()
with open(current_file.parent / 'part_b.html', 'w') as f:
    f.write(fig.to_html())
