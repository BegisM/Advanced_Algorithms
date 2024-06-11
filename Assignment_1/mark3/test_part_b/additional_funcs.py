def generate_large_text(text, size_kb):
    # Generate a large text with the specified size in kilobytes
    repeat_factor = (size_kb * 1024) // len(text)
    large_text = text * repeat_factor
    return large_text

