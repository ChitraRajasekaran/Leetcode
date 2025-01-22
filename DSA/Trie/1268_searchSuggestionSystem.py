from typing import List, Optional

class Trie:
    def __init__(self):
        # Initialize each node with an array of 26 elements representing 26 characters, setting each to None.
        # Each node stores a list of integer indices which represent suggested products.
        self.children: List[Optional[Trie]] = [None] * 26
        self.indices: List[int] = []

    def insert(self, word: str, index: int):
        # Insert a word into the trie with its associated product index.
        node = self
        for char in word:
            char_index = ord(char) - ord('a')
            if node.children[char_index] is None:
                node.children[char_index] = Trie()
            node = node.children[char_index]
            # Insert product index into the current trie node's list if fewer than 3 suggestions.
            if len(node.indices) < 3:
                node.indices.append(index)

    def search(self, word: str) -> List[List[int]]:
        # Return a list of product index lists for each character in the searched word.
        node = self
        results = [[] for _ in range(len(word))]
        for i, char in enumerate(word):
            char_index = ord(char) - ord('a')
            # Break early if no path in the trie exists for the current character.
            if node.children[char_index] is None:
                break
            node = node.children[char_index]
            # Add the current node's product indices to the results.
            results[i] = node.indices
        return results


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products to ensure the lexicographically smallest suggestions.
        products.sort()
        trie = Trie()
        # Insert each product into the trie along with its index.
        for index, word in enumerate(products):
            trie.insert(word, index)
        # Get the list of product indices from the trie for each substring of the search word.
        indices_list = trie.search(searchWord)
        # Convert the list of product indices to a list of product strings.
        return [[products[index] for index in indices_sublist] for indices_sublist in indices_list]
