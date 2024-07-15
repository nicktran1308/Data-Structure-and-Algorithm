"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1
        return res


"""
Boyer-Moore Voting Algorithm

Time Complexity: O(n) - each element is visited once
Space Complexity: O(1) - constant space


Input: nums = [2, 2, 1, 1, 1, 2, 2]

Detailed Execution:
    Initialization:

        First Element (2):
            count is 0, update res to 2.
            Increment count (count = 1).
        Second Element (2):
            n equals res.
            Increment count (count = 2).
        Third Element (1):
            n does not equal res.
            Decrement count (count = 1).
        Fourth Element (1):
            n does not equal res.
            Decrement count (count = 0).
        Fifth Element (1):
            count is 0, update res to 1.
            Increment count (count = 1).
        Sixth Element (2):
            n does not equal res.
            Decrement count (count = 0).
        Seventh Element (2):
            count is 0, update res to 2.
            Increment count (count = 1).
    Result:
        The candidate res at the end of the iteration is 2, which is returned as the majority element.

"""
