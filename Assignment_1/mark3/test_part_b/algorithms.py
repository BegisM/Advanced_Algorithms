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


def binary_sunday_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    shift = {pattern[i]: m - i for i in range(m)}
    i = 0
    while i <= n - m:
        if text[i:i + m] == pattern:
            return i
        if i + m < n:
            i += shift.get(text[i + m], m + 1)
        else:
            break
    return -1


def gusfield_z_search(text, pattern):
    def compute_z(s):
        Z = [0] * len(s)
        L, R, K = 0, 0, 0
        for i in range(1, len(s)):
            if i > R:
                L, R = i, i
                while R < len(s) and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
            else:
                K = i - L
                if Z[K] < R - i + 1:
                    Z[i] = Z[K]
                else:
                    L = i
                    while R < len(s) and s[R] == s[R - L]:
                        R += 1
                    Z[i] = R - L
                    R -= 1
        return Z

    concatenated = pattern + '$' + text
    Z = compute_z(concatenated)
    m = len(pattern)
    for i in range(m + 1, len(concatenated)):
        if Z[i] == m:
            print(f"Gusfield Z match at index {i - m - 1}")
            return i - m - 1
    return -1