import random
import string


def generate_rabin_karp_test_text(pattern_length, text_length, pattern_frequency):
    # Generate a random pattern of the specified length
    large_alphabet = string.ascii_letters + string.digits + string.punctuation
    pattern = ''.join(random.choices(large_alphabet, k=pattern_length))

    # Create the initial part of the text with random characters
    text = ''.join(random.choices(large_alphabet, k=text_length))

    # Insert the pattern into the text at random positions
    positions = sorted(random.sample(range(text_length - pattern_length), pattern_frequency))
    for pos in positions:
        text = text[:pos] + pattern + text[pos + pattern_length:]

    # Introduce hash collision sequences in the text
    # We'll create some sequences that differ slightly from the pattern
    # but could still have the same hash (e.g., by changing a character)
    for _ in range(pattern_frequency // 2):
        collision_seq = list(pattern)
        random.shuffle(collision_seq)
        collision_seq = ''.join(collision_seq)
        pos = random.randint(0, text_length - pattern_length)
        text = text[:pos] + collision_seq + text[pos + pattern_length:]

    return text, pattern


if __name__ == '__main__':
    # Example usage:
    pattern_length = 10
    text_length = 200
    pattern_frequency = 5

    text, pattern = generate_rabin_karp_test_text(pattern_length, text_length, pattern_frequency)
    print("Generated Pattern:", pattern)
    print("Generated Text:", text)
