from Assignment_1.mark3.algorithms import sunday_search, kmp_search, rabin_karp_search, gusfield_z_search
from Assignment_1.mark3.part_A.additional_funcs import measure_time, generate_text


specific_text_length = 100000  # 100KB


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


# Generate a specific text and pattern for each case
def generate_case_1():
    T = "a" * (specific_text_length - 50) + "b" * 50
    P = "b" * 50  # Specific pattern for Binary Sunday vs Gusfield Z
    return T, P


def generate_case_2():
    T = "a" * (specific_text_length - 50) + "b" * 50
    P = "a" * 25 + "b" * 25  # Specific pattern for KMP vs Rabin-Karp
    return T, P


def generate_case_3():
    T = "a" * (specific_text_length - 50) + "b" * 50
    P = "a" * 49 + "b"  # Specific pattern for Rabin-Karp vs Sunday
    return T, P


def prove_case(algorithm1, algorithm2, case_func):
    T, P = case_func()
    time1 = measure_time(algorithm1, T, P)
    time2 = measure_time(algorithm2, T, P)
    return time1, time2


# Case 1: Binary Sunday vs Gusfield Z
time_binary_sunday, time_gusfield_z = prove_case(binary_sunday_search, gusfield_z_search, generate_case_1)
print(f"Binary Sunday: {time_binary_sunday}, Gusfield Z: {time_gusfield_z}")

# Case 2: KMP vs Rabin-Karp
time_kmp, time_rabin_karp = prove_case(kmp_search, rabin_karp_search, generate_case_2)
print(f"KMP: {time_kmp}, Rabin-Karp: {time_rabin_karp}")

# Case 3: Rabin-Karp vs Sunday
time_rabin_karp_2, time_sunday_2 = prove_case(rabin_karp_search, sunday_search, generate_case_3)
print(f"Rabin-Karp: {time_rabin_karp_2}, Sunday: {time_sunday_2}")

# Explanation of results:
print("\nExplanations:")
if time_binary_sunday < 0.5 * time_gusfield_z:
    print("Binary Sunday is at least twice as fast as Gusfield Z in this case.")
else:
    print("Gusfield Z is not slower than Binary Sunday by a factor of two in this case.")

if time_kmp < 0.5 * time_rabin_karp:
    print("KMP is at least twice as fast as Rabin-Karp in this case.")
else:
    print("Rabin-Karp is not slower than KMP by a factor of two in this case.")

if time_rabin_karp_2 < 0.5 * time_sunday_2:
    print("Rabin-Karp is at least twice as fast as Sunday in this case.")
else:
    print("Sunday is not slower than Rabin-Karp by a factor of two in this case.")
