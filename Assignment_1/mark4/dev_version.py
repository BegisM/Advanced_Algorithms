def match_bruteforce(text, pattern):
    def matches(text_char, pattern_char):
        if pattern_char == '?':
            return True
        return text_char == pattern_char

    def pattern_matches(text, pattern):
        i, j = 0, 0
        while j < len(pattern):
            if pattern[j] == '\\':
                j += 1
                if j < len(pattern) and pattern[j] in ['?', '*', '\\']:
                    if i >= len(text) or text[i] != pattern[j]:
                        return False
                    i += 1
                    j += 1
                else:
                    return False
            elif pattern[j] == '?':
                if i >= len(text):
                    return False
                i += 1
                j += 1
            elif pattern[j] == '*':
                j += 1
                if j == len(pattern):
                    return True
                while i < len(text):
                    if pattern_matches(text[i:], pattern[j:]):
                        return True
                    i += 1
                return False
            else:
                if i >= len(text) or not matches(text[i], pattern[j]):
                    return False
                i += 1
                j += 1
        return i == len(text)

    for i in range(len(text) + 1 - len(pattern.replace('*', ''))):
        if pattern_matches(text[i:], pattern):
            return True
    return False


def build_sunday_shift_table(pattern):
    last_occurrence = {}
    m = len(pattern)
    for i, char in enumerate(pattern):
        last_occurrence[char] = i
    return last_occurrence


def match_sunday(text, pattern):
    def matches(text_char, pattern_char):
        if pattern_char == '?':
            return True
        return text_char == pattern_char

    def pattern_matches(text, pattern):
        i, j = 0, 0
        while j < len(pattern):
            if pattern[j] == '\\':
                j += 1
                if j < len(pattern) and pattern[j] in ['?', '*', '\\']:
                    if i >= len(text) or text[i] != pattern[j]:
                        return False
                    i += 1
                    j += 1
                else:
                    return False
            elif pattern[j] == '?':
                if i >= len(text):
                    return False
                i += 1
                j += 1
            elif pattern[j] == '*':
                j += 1
                if j == len(pattern):
                    return True
                while i < len(text):
                    if pattern_matches(text[i:], pattern[j:]):
                        return True
                    i += 1
                return False
            else:
                if i >= len(text) or not matches(text[i], pattern[j]):
                    return False
                i += 1
                j += 1
        return i == len(text)

    m = len(pattern)
    n = len(text)
    shift_table = build_sunday_shift_table(pattern)
    skip = m - shift_table.get('*', m)  # Treat '*' as a special character

    i = 0
    while i <= n - m:
        if pattern_matches(text[i:], pattern):
            return True
        next_pos = i + m
        if next_pos < n:
            i += m - shift_table.get(text[next_pos], -1)
        else:
            break
    return False


# Test cases for the algorithms
test_cases = [
    ("abcde", "a?c*", True),
    ("hello world", "he*o w?rld", True),
    ("abcd", "a\\*bc\\?d", False),
    ("abc*def", "abc\\*def", True),
    ("abc?def", "abc\\?def", True),
    ("", "*", True),
    ("", "?", False),
    ("abc", "\\*", False),
    ("aaaabbbbcccc", "a*b*c", True),
    ("aabcc", "a*b*", True),
]

# Testing Brute-force Algorithm
print("Testing Brute-force Algorithm:")
for text, pattern, expected in test_cases:
    result = match_bruteforce(text, pattern)
    print(f"Text: {text}, Pattern: {pattern}, Match: {result}, Expected: {expected}")

# Testing Sunday Algorithm
print("\nTesting Sunday Algorithm:")
for text, pattern, expected in test_cases:
    result = match_sunday(text, pattern)
    print(f"Text: {text}, Pattern: {pattern}, Match: {result}, Expected: {expected}")