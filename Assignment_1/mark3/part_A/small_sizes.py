from ploting import plot_results
from additional_funcs import run_experiments
from Assignment_1.mark3.algorithms import (brute_force_search, sunday_search, kmp_search, fsm_search, rabin_karp_search,
                                           gusfield_z_search)

algorithms = [
    ("Brute-force", brute_force_search),
    ("Sunday", sunday_search),
    ("KMP", kmp_search),
    ("FSM", fsm_search),
    ("Rabin-Karp", rabin_karp_search),
    ("Gusfield Z", gusfield_z_search)
]


text_lengths = [i for i in range(10, 101, 10)]
small_pattern = "computer"


results_small = run_experiments(algorithms, text_lengths, small_pattern)

for k, i in results_small.items():
    print(f'{[x*10**6 for x in i]}')

plot_results(results_small, 'Running Time vs Text Length (Small Pattern)', text_lengths, adjust_dimensions=True)
