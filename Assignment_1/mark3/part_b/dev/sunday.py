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
