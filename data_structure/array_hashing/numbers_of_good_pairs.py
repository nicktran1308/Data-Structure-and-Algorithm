"""
Numbers of Good Pairs


Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = Counter(nums)

        for val in freq.values():
            if val > 1:
                # If there are 'val' instances of a number, then we can choose 2 out of 'val' for a good pair
                count += val * (val - 1) // 2

        return count


"""
Time Complexity: O(n) n - number of elements in 'nums'
Space Complexity:O(u) u - number of unique elements in 'nums'

** C (n, 2) = n x (n-1) / 2

Steps:
    nums = [1,2,3,1,1,3]

    Frequencies:
        1 appears 3 times.
        2 appears 1 time.
        3 appears 2 times.
    Counting Pairs:
        For 1, the number of good pairs is 3 * (3 - 1) // 2 = 3.
        For 2, no pairs can be formed since it appears only once.
        For 3, the number of good pairs is 2 * (2 - 1) // 2 = 1.
        Total Good Pairs: 3 (from '1') + 0 (from '2') + 1 (from '3') = 4.
"""
