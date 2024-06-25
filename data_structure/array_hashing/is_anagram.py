"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # Check if the length of the strings are equal
            return False

        count_s = {}  # Dictionary to store count of each character in string s
        count_t = {}  # Dictionary to store count of each character in string t

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(
                s[i], 0
            )  # Count of each character in string s
            count_t[t[i]] = 1 + count_t.get(
                t[i], 0
            )  # Count of each character in string t
        return (
            count_s == count_t
        )  # Compare the two dictionaries to check if they are equal


"""
Time Complexity: O(n) - n: length of strings s & t. Algorithm makes 1 pass though the strings to count.
Space Complexity: O(1) - Limited to number of lower case English letters.

Steps:
    a. Check if the length of the strings are equal
    b. Create a dictionary to store count of each character in string s
    c. count_s[s[i]] = 1 + count_s.get(s[i], 0)
        c1. count character in s to put in dictionary, if it is not in the dictionary, it will be set to 1.
            if it's in the dictionary, we will compare it with 0 so 1 + count_s.get(s[i], 0)
    d. Same for string t
    e. Compare the two dictionaries to check if they are equal
"""
