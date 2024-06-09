from algorithms import brute_force_search_with_wildcards, sunday_search_with_wildcards

text = "abacdabcda"
pattern = "a?c*d"

print(brute_force_search_with_wildcards(text, pattern))  # Should print True
print(sunday_search_with_wildcards(text, pattern))      # Should print True