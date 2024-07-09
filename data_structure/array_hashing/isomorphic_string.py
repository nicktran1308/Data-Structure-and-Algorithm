"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s, map_t = {}, {}

        for i, j in zip(s, t):
            if (i in map_s and map_s[i] != j) or (j in map_t and map_t[j] != i):
                return False
            map_s[i] = j
            map_t[j] = i
        return True


"""
Time Complexity: O(n), where n is the length of the input string
Space Complexity: O(m), worst case m is all unique characters which can be 256 (ASCII characters) 

Initialization: Two empty dictionaries, map_s and map_t, are created.
    Iteration over characters:
        First pair ('e', 'a'):
        Neither 'e' nor 'a' is in map_s or map_t.
        Set map_s['e'] = 'a' and map_t['a'] = 'e'.

        Second pair ('g', 'd'):
        Neither 'g' nor 'd' is in map_s or map_t.
        Set map_s['g'] = 'd' and map_t['d'] = 'g'.

        Third pair ('g', 'd') again:
        Both 'g' and 'd' are already in map_s and map_t.
        Check if map_s['g'] == 'd' and map_t['d'] == 'g', both conditions are true.

        Final output: True. The characters consistently map to each other.
"""
