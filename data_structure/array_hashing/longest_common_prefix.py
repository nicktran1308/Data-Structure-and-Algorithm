"""
14. Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""  # Create an empty string as result
        for i in range(len(strs[0])):  # Iterate through the first string
            for s in strs:  # Iterate through the rest of the string
                if (
                    i == len(s) or s[i] != strs[0][i]
                ):  # If the index is out of range or the character is not equal to the first string
                    return result  # Return result
            result += strs[0][i]  # Add the character to the result
        return result  # Return the result


"""
Time Complexity: O(n*m) - n is the number of strings and m is the length of the longest string
Space Complexity: O(1) - no extra space is used

Steps:

    1.  Loop through the characters of the first string "flower"
        i = 0, character = "f"
        Check each string in 'strs' to see if the character is equal to the first string
        'flower'[0] = 'f'
        'flow'[0] = 'f'
        'flight'[0] = 'f'
        Since all match, append 'f' to 'result'
    
    'for i in range(len(strs[0])):' - iterate through the characters of the first string 'flower' f,l,o,w,e,r i = 0 -5
    'for s in strs:' - iterate through each string in strs 'flower', 'flow', 'flight'

    Here, s[i] != strs[0][i] translates to:

    For "flow": s[2] != strs[0][2] is o != o, which is False.
    For "flight": s[2] != strs[0][2] is i != o, which is True.
"""
