from Assignment_1.algorithms import sunday_search, kmp_search, rabin_karp_search, gusfield_z_search
from Assignment_1.mark3.part_A.additional_funcs import measure_time, generate_text

specific_text_length = 100000  # 100KB


# Generate a specific text and pattern for each case
def generate_case_1():
    T = generate_text(specific_text_length)
    P = "a" * 50  # Pattern repeated in text
    return T, P


def generate_case_2():
    T = generate_text(specific_text_length)
    P = "b" * 50  # Pattern repeated in text
    return T, P


def generate_case_3():
    T = generate_text(specific_text_length)
    P = "c" * 50  # Pattern repeated in text
    return T, P


def prove_case(algorithm1, algorithm2, case_func):
    T, P = case_func()
    time1 = measure_time(algorithm1, T, P)
    time2 = measure_time(algorithm2, T, P)
    return time1, time2


# Case 1: Binary Sunday vs Gusfield Z
T1, P1 = generate_case_1()
time_binary_sunday, time_gusfield_z = prove_case(sunday_search, gusfield_z_search, generate_case_1)
print(f"Binary Sunday: {time_binary_sunday}, Gusfield Z: {time_gusfield_z}")

# Case 2: KMP vs Rabin-Karp
T2, P2 = generate_case_2()
time_kmp, time_rabin_karp = prove_case(kmp_search, rabin_karp_search, generate_case_2)
print(f"KMP: {time_kmp}, Rabin-Karp: {time_rabin_karp}")

# Case 3: Rabin-Karp vs Sunday
T3, P3 = generate_case_3()
time_rabin_karp_2, time_sunday_2 = prove_case(rabin_karp_search, sunday_search, generate_case_3)
print(f"Rabin-Karp: {time_rabin_karp_2}, Sunday: {time_sunday_2}")
