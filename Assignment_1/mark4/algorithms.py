def match(text, pattern, ti, pi):
    while ti < len(text) and pi < len(pattern):
        if pattern[pi] == '\\':  # Escape character
            pi += 1
            if pi >= len(pattern):
                return False
            if pattern[pi] != text[ti]:
                return False
        elif pattern[pi] == '?':
            pi += 1
            ti += 1
        elif pattern[pi] == '*':
            if pi + 1 < len(pattern) and pattern[pi + 1] == '\\':  # Handle escaped wildcards
                pi += 2
                if pi < len(pattern) and pattern[pi] != text[ti]:
                    return False
                ti += 1
            else:
                # Try to match zero or more characters
                for k in range(len(text) - ti + 1):
                    if match(text, pattern, ti + k, pi + 1):
                        return True
                return False
        else:
            if pattern[pi] != text[ti]:
                return False
            pi += 1
            ti += 1
    # Check if the entire pattern was matched
    while pi < len(pattern) and pattern[pi] == '*':
        pi += 1
    return pi == len(pattern)


def brute_force_search_with_wildcards(text, pattern):
    for i in range(len(text)):
        if match(text, pattern, i, 0):
            return True
    return False


def sunday_search_with_wildcards(text, pattern):
    def get_shift_table(pattern):
        shift = {c: len(pattern) + 1 for c in set(text)}
        for i, char in enumerate(pattern):
            shift[char] = len(pattern) - i
        return shift

    shift = get_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        if match(text, pattern, i, 0):
            return True
        if i + len(pattern) < len(text):
            i += shift.get(text[i + len(pattern)], len(pattern) + 1)
        else:
            break
    return False
