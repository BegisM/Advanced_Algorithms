from pathlib import Path

from assignment_2_spell_checker.utils.draw_plot import plot_results
from dictionary.naive import NaiveDictionary
from dictionary.bbst import BBSTDictionary
from dictionary.trie import TrieDictionary
from dictionary.hashmap import HashMapDictionary
from labyrinth.wizard_race import WizardRace
from utils.timer import Timer


def line(n=20):
    print("* "*n)


def main():
    current_file = Path(__file__).resolve()
    current_directory = current_file.parent

    dictionary_file = current_directory / "data" / "english_words.txt"
    text_file = current_directory / "data" / "2600-0.txt"

    print(f"Dictionary file: {dictionary_file.name}")
    print(f"Text file for spell checking: {text_file.name}\n")

    # Dictionary implementations
    naive_dict = NaiveDictionary()
    bbst_dict = BBSTDictionary()
    trie_dict = TrieDictionary()
    hashmap_dict = HashMapDictionary()

    # Load dictionaries
    Timer.time_function(naive_dict.load, "Naive Dictionary Load", dictionary_file)
    Timer.time_function(bbst_dict.load, "BBST Dictionary Load", dictionary_file)
    Timer.time_function(trie_dict.load, "Trie Dictionary Load", dictionary_file)
    Timer.time_function(hashmap_dict.load, "HashMap Dictionary Load", dictionary_file)

    # Spell checking
    Timer.time_function(naive_dict.spell_check, "Naive Dictionary Spell Check", text_file)
    Timer.time_function(bbst_dict.spell_check, "BBST Dictionary Spell Check", text_file)
    Timer.time_function(trie_dict.spell_check, "Trie Dictionary Spell Check", text_file)
    Timer.time_function(hashmap_dict.spell_check, "HashMap Dictionary Spell Check", text_file)

    print("\nSummary of Results:")
    for description, time_taken in Timer.results:
        print(f"{description}: {time_taken:.4f} seconds")

    # Labyrinth wizard race
    labyrinth = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': ['E']
    }

    wizards = ['A', 'B', 'C']
    speeds = [1, 2, 1.5]

    line()

    print("Labyrinth Map:", labyrinth)
    print("Wizards' Initial Positions:", wizards)
    print("Wizards' Speeds (in corridors per minute):", speeds)

    race = WizardRace(labyrinth, 'E')
    winner = race.predict_winner(wizards, speeds)
    print(f"\nThe wizard who will reach the exit first is: {winner}")

    # Plot the results
    plot_results(Timer.results)


if __name__ == '__main__':
    main()
