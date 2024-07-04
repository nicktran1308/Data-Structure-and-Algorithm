"""
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(
            list
        )  # Store list of anagrams. If a key doesn't exist, return a new list by default,

        for s in strs:
            count = [0] * 26  # Create a list count of 26 zeros.
            for c in s:
                count[ord(c) - ord("a")] += 1
                answer[tuple(count)].append(s)
            return answer.values()


"""
Time Complexity: O(n*k)
Space Complexity: O(n*k)

Steps:
    1. Create a list of anagrams. If a key doesn't exist, return a new list by default
    2. Loop through each string in strs.
    3. Create a list count of 26 zeros.
    4. Loop through each character in the string.
    5. Increment count[ord(c) - ord('a')] += 1
        ord() function returns the Unicode code point of a one-character string. ord(a) == 97, ord(b) == 98, ord(c) == 99,...
    6. Return answer.values()


Example:
    String "act":

    Initialize count = [0, 0, 0, ..., 0] (26 zeros).
    Increment positions for 'a', 'c', and 't'.
    After processing "act", count becomes [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0].
    Convert count to a tuple and use it as a key in ans.
    ans[(1, 0, 1, ..., 1)] = ["act"].

    
    String "cat":

    Process similar to "act" since it's an anagram.
    Same count as "act".
    Append "cat" to the existing list: ans[(1, 0, 1, ..., 1)] = ["act", "cat"].
"""
