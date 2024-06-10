class HashMapDictionary:
    def __init__(self):
        self.words = set()

    def load(self, dictionary_file):
        with open(dictionary_file, 'r') as file:
            self.words.update(line.strip() for line in file)

    def spell_check(self, text_file):
        with open(text_file, 'r') as file:
            text = file.read().split()
        misspelled = [word for word in text if word not in self.words]
        return misspelled