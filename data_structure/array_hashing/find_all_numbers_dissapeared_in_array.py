"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark each number as visited by negating its value & corresponding index
        for nums in nums:
            idx = abs(nums) - 1  # Get the index from the number
            if nums[idx] > 0:  # If not already marked, negate it
                nums[idx] = -nums[idx]

        # Collect all indices where numbers are positive (not visited)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)  # i + 1 gives the actual number

        return res


"""
Time Complexity: O(n) - 1st loop runs through all 'n' elements once, 2nd loop runs through all 'n' elements once.
Space Complexity: O(1) - No extra space is used.

Steps:
    Input: nums = [4,3,2,7,8,2,3,1]
        
        First Element (4):
            Calculate the index: abs(4) - 1 = 3.
            Negate the element at index 3: nums[3] changes from 7 to -7.
            Updated nums: [4, 3, 2, -7, 8, 2, 3, 1].
        
        Second Element (3):
            Calculate the index: abs(3) - 1 = 2.
            Negate the element at index 2: nums[2] changes from 2 to -2.
            Updated nums: [4, 3, -2, -7, 8, 2, 3, 1].
        
        Third Element (2):
            Calculate the index: abs(2) - 1 = 1.
            Negate the element at index 1: nums[1] changes from 3 to -3.
            Updated nums: [4, -3, -2, -7, 8, 2, 3, 1].

        Fourth Element (-7):
            Calculate the index: abs(-7) - 1 = 6.
            Negate the element at index 6: nums[6] changes from 3 to -3.
            Updated nums: [4, -3, -2, -7, 8, 2, -3, 1].
        ....

        Updated nums: [4, -3, -2, -7, 8, 2, -3, -1].

        nums[4] = 8 and nums[5] = 2 are the only positive values in the updated array.
        The indices 4 and 5 correspond to numbers 5 and 6

        => Output is [5,6]
"""
