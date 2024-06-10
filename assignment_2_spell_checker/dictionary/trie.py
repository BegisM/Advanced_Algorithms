class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class TrieDictionary:
    def __init__(self):
        self.trie = Trie()

    def load(self, dictionary_file):
        with open(dictionary_file, 'r') as file:
            for line in file:
                self.trie.insert(line.strip())

    def spell_check(self, text_file):
        with open(text_file, 'r') as file:
            text = file.read().split()
        misspelled = [word for word in text if not self.trie.search(word)]
        return misspelled