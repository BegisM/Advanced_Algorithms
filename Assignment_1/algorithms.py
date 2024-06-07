def brute_force_search(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Brute-force match at index {i}")
            return i
    return -1


def sunday_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    shift = {c: m + 1 for c in set(text)}
    for i in range(m):
        shift[pattern[i]] = m - i

    i = 0
    while i <= n - m:
        if text[i:i + m] == pattern:
            print(f"Sunday match at index {i}")
            return i
        if i + m >= n:
            return -1
        i += shift.get(text[i + m], m + 1)
    return -1


def kmp_search(text, pattern):
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
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
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print(f"KMP match at index {i - j}")
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def fsm_search(text, pattern):
    def compute_fsm(pattern):
        m = len(pattern)
        fsm = [{} for _ in range(m + 1)]
        for state in range(m + 1):
            for x in set(text):  # Consider all possible characters in the text
                k = min(m, state + 1)
                while k > 0 and not pattern[:k].endswith(pattern[state - k + 1:state] + x):
                    k -= 1
                fsm[state][x] = k
        return fsm

    fsm = compute_fsm(pattern)
    state = 0
    for i, char in enumerate(text):
        state = fsm[state].get(char, 0)
        if state == len(pattern):
            print(f"FSM match at index {i - len(pattern) + 1}")
            return i - len(pattern) + 1
    return -1


def rabin_karp_search(text, pattern, q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                print(f"Rabin-Karp match at index {i}")
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
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
