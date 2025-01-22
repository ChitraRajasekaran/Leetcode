from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character in the input string
        char_frequency = Counter(s)
      
        # Sort the characters based on frequency in descending order
        sorted_characters = sorted(char_frequency.items(), key=lambda item: -item[1])
      
        # Create a string with characters repeated by their frequency
        frequency_sorted_string = ''.join(character * frequency for character, frequency in sorted_characters)
      
        return frequency_sorted_string

# Example usage:
# sol = Solution()
# result = sol.frequencySort("tree")
# print(result)  # Outputs a string with characters sorted by frequency, e.g. "eetr"
