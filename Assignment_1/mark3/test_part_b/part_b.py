from Assignment_1.mark3.test_part_b.algorithms import (kmp_search, binary_sunday_search, gusfield_z_search,
                                                       rabin_karp_search)
from Assignment_1.mark3.part_A.additional_funcs import measure_time   # , generate_text
from Assignment_1.mark3.test_part_b.additional_funcs import generate_large_text as generate_text

specific_text_length = 100  # 100KB
TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "


# Generate a specific text and pattern for each case
def generate_case_1():
    global TEXT
    T = generate_text(TEXT, specific_text_length)
    P = 'ipsum'
    # P = T[:50]  # Specific pattern for Binary Sunday vs Gusfield Z
    return T, P
#
#
# def generate_case_2():
#     global text
#     T = generate_text(text, specific_text_length)
#     P = "b" * 50  # Specific pattern for KMP vs Rabin-Karp
#     return T, P
#
#
# def generate_case_3():
#     T = generate_text(specific_text_length)
#     P = "c" * 50  # Specific pattern for Rabin-Karp vs Sunday
#     return T, P


def prove_case(algorithm1, algorithm2, case_func):
    T, P = case_func()
    time1 = measure_time(algorithm1, T, P)
    time2 = measure_time(algorithm2, T, P)
    return time1, time2


# Case 1: Binary Sunday vs Gusfield Z
time_binary_sunday, time_gusfield_z = prove_case(binary_sunday_search, gusfield_z_search, generate_case_1)
print(f"Binary Sunday: {time_binary_sunday}, Gusfield Z: {time_gusfield_z}")

# Case 2: KMP vs Rabin-Karp
time_kmp, time_rabin_karp = prove_case(kmp_search, rabin_karp_search, generate_case_1)
print(f"KMP: {time_kmp}, Rabin-Karp: {time_rabin_karp}")

# Case 3: Rabin-Karp vs Sunday
time_rabin_karp_2, time_sunday_2 = prove_case(rabin_karp_search, binary_sunday_search, generate_case_1)
print(f"Rabin-Karp: {time_rabin_karp_2}, Sunday: {time_sunday_2}")

# Explanation of results:
print("\nExplanations:")
if time_binary_sunday <= 0.5 * time_gusfield_z:
    print("Binary Sunday is at least twice as fast as Gusfield Z in this case.")
else:
    print("Gusfield Z is not slower than Binary Sunday by a factor of two in this case.")

if time_kmp <= 0.5 * time_rabin_karp:
    print("KMP is at least twice as fast as Rabin-Karp in this case.")
else:
    print("Rabin-Karp is not slower than KMP by a factor of two in this case.")

if time_rabin_karp_2 <= 0.5 * time_sunday_2:
    print("Rabin-Karp is at least twice as fast as Sunday in this case.")
else:
    print("Sunday is not slower than Rabin-Karp by a factor of two in this case.")
