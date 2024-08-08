"""
Maximum Number of Ballons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0

"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textcounter = Counter(text)
        balloon = Counter("balloon")

        res = len(text)

        for c in balloon:
            res = min(res, textcounter[c] // balloon[c])
        return res


"""
Time Complexity: O(n + m) - n: length of text, m: length of balloon
Space Complexity: O(U) - U: unique characters in "text" and "balloon" - use to store character counts

Steps:
        Input: text = "nlaebolko"

        Counter Initialization:

            countText = Counter({'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1})
            balloon = Counter({'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1})

        Loop Execution:

            Start with res = len(text) = 9.
            For 'b': min(9, countText['b'] // balloon['b']) = min(9, 1 // 1) = 1
            For 'a': min(1, countText['a'] // balloon['a']) = min(1, 1 // 1) = 1
            For 'l': min(1, countText['l'] // balloon['l']) = min(1, 2 // 2) = 1
            For 'o': min(1, countText['o'] // balloon['o']) = min(1, 2 // 2) = 1
            For 'n': min(1, countText['n'] // balloon['n']) = min(1, 1 // 1) = 1
            
        Result:

            The loop confirms that "balloon" can be formed only once, so res = 1.
"""
