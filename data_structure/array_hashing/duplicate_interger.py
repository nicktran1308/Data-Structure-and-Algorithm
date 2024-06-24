"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create a set to store seen elements
        for num in nums:  # Loop through the array
            if num in seen:
                return True  # If the element is in the set, return True
            else:
                seen.add(
                    num
                )  # If the element is not in the set, add the element to the set
        return False  # Return False at the end


"""
Time Complexity: O(n)      ( only loop through the array once, 'in' and 'add' are O(1) )
Space Complexity: O(n)     ( worst case: all elements are unique, so set will have n elements )

Steps:
    1. Create a set to store seen elements
    2. Loop through the array
    3. If the element is in the set, return True
    4. If the element is not in the set, add the element to the set
    5. Return False at the end

"""
