import time


def kmp_search(text, pattern):
    # KMP algorithm implementation
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    lps = [0] * m
    j = 0  # index for pattern
    i = 0  # index for text
    compute_lps(pattern, m, lps)
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
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def rabin_karp_search(text, pattern):
    # Rabin-Karp algorithm implementation
    d = 256  # number of characters in the input alphabet
    q = 101  # a prime number

    n = len(text)
    m = len(pattern)
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, m-1)%q"
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match, then only check for characters one by one
        if p == t:
            # Check for characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

    return -1


def generate_large_text(size_kb):
    # Generate a large text with the specified size in kilobytes
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    repeat_factor = (size_kb * 1024) // len(text)
    large_text = text * repeat_factor
    return large_text


def begis(num):
    # Generate a large text of at least 100kB
    large_text = generate_large_text(num)

    # Create a pattern that occurs multiple times within the large text
    pattern = "ipsum"

    # Measure execution times for KMP and Rabin-Karp
    start_time_kmp = time.time()
    kmp_found = kmp_search(large_text, pattern)
    end_time_kmp = time.time()

    start_time_rabin_karp = time.time()
    rabin_karp_found = rabin_karp_search(large_text, pattern)
    end_time_rabin_karp = time.time()

    # Compare execution times
    kmp_time = end_time_kmp - start_time_kmp
    rabin_karp_time = end_time_rabin_karp - start_time_rabin_karp

    # Check if KMP is at least twice as fast as Rabin-Karp
    if kmp_time * 2 <= rabin_karp_time:
        # print("KMP is at least twice as fast as Rabin-Karp.")
        # print("Text Length:", len(large_text))
        # print("Pattern:", pattern)
        # print("KMP Time:", kmp_time)
        # print("Rabin-Karp Time:", rabin_karp_time)
        return 1, large_text, pattern
    else:
        # print("KMP is not at least twice as fast as Rabin-Karp.")
        return 0, None, None



res = begis(10000000)
while not res[0]:
    res = begis(100000)
    print('well')
else:
    print(res[1], res[2], sep='\n\n\n\n')