from ploting import plot_results
from additional_funcs import run_experiments
from Assignment_1.mark3.part_A.algorithms import (brute_force_search, sunday_search, kmp_search, rabin_karp_search,
                                                  gusfield_z_search, fsm_search)

algorithms = [
    ("Brute-force", brute_force_search),
    ("Sunday", sunday_search),
    ("KMP", kmp_search),
    # ("FSM", fsm_search),
    ("Rabin-Karp", rabin_karp_search),
    ("Gusfield Z", gusfield_z_search)
]


text_lengths = [10_000, 50_000, 100_000, 500_000]
large_pattern = " " * 100  # Assuming space as a repeated character for simplicity


results_large = run_experiments(algorithms, text_lengths, large_pattern)

for k, i in results_large.items():
    print(f'{i}')

plot_results(results_large, 'Running Time vs Text Length (Large Pattern)', text_lengths)
