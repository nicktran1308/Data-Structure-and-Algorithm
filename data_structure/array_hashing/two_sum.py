"""
Two Integer Sum


Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # store number and its index

        for i, num in enumerate(nums):  # useful for both the value and index
            diff = target - num
            if diff in num_map:  # Check if the difference is in the num_map
                return [num_map[diff], i]  # Return the index of the difference
            num_map[num] = i  # Add the number and its index to the map
        return []


"""
Time Complexity: O(n) - traverse the array once
Space Complexity: O(n) - Worst case might need to store all the numbers in the num_map

Steps:
    Step 1: i = 0, num = 3
        Calculate complement = 7 - 3 = 4.
        Check if 4 is in num_map. It's not.
        Add 3 to num_map with its index: num_map = {3: 0}.

    Step 2: i = 1, num = 4
        Calculate complement = 7 - 4 = 3.
        Check if 3 is in num_map. It is, and it was found at index 0.
        Since the complement (3) exists in the dictionary, and its index is 0, we return [0, 1] as the result because the sum of nums[0] and nums[1] equals 7.
"""
