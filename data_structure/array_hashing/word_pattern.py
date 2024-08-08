"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        if len(words) != len(pattern):
            return False  # Early return if the number of elements don't match

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if (char in char_to_word and char_to_word[char] != word) or (
                word in word_to_char and word_to_char[word] != char
            ):
                return False  # Return False if there's a mismatch
            char_to_word[char] = word
            word_to_char[word] = char

        return True


"""
Time Complexity: O(n) - n is the length of the input string s.
Space Complexity: O(m + k) - m is the number of unique characters in pattern and k is the number of unique words in 's'

Steps:
    Input: pattern = "abba", s = "dog cat cat dog"

    Step-by-Step Execution:

        Split s into words: words = ['dog', 'cat', 'cat', 'dog']

        Check length correspondence: Both pattern and words have a length of 4, so we proceed.

        Initialize dictionaries: char_to_word and word_to_char for mapping.

        Iterate through pattern and words:
            Iteration 1: char = 'a', word = 'dog'
                Both char and word are new, add to dictionaries: {a: dog}, {dog: a}
            Iteration 2: char = 'b', word = 'cat'
                Both are new, add to dictionaries: {a: dog, b: cat}, {dog: a, cat: b}
            Iteration 3: char = 'b', word = 'cat'
                Already in dictionaries and correct mapping, continue.
            Iteration 4: char = 'a', word = 'dog'
            Already in dictionaries and correct mapping, continue.

         Return True: No mismatches found, pattern matches s
"""
