"""
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Counter for the number of flowers we can plant
        length = len(flowerbed)

        for i in range(length):
            # Check if current plot is empty and adjacent plots are also empty or boundaries
            if flowerbed[i] == 0:
                # Safe to consider left and right only if within bounds and they are also empty
                empty_left = i == 0 or flowerbed[i - 1] == 0
                empty_right = i == length - 1 or flowerbed[i + 1] == 0

                if empty_left and empty_right:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    # If we have planted enough flowers, return true
                    if count >= n:
                        return True

        # If we finish the loop and haven't planted enough flowers
        return count >= n


"""
Time Complexity: O(n), where n is the length of the flowerbed array
Space Complexity: O(1), no additional space is used
Steps:
    Initialization: count = 0, length = 5.
        Iteration over Flowerbed:
            Index 0: i = 0, plot has a flower, skip.
            Index 1: i = 1, plot is empty.
            
            empty_left = False (previous plot has a flower).
            empty_right = True (next plot is empty).
            Both conditions are not met; skip.
            
            
            Index 2: i = 2, plot is empty.
            empty_left = True (previous plot is empty).
            empty_right = True (next plot is empty).
            Both conditions are met; plant a flower here: flowerbed[2] = 1, count = 1.

            Continue because count < n.
            
            Index 3: i = 3, now has a neighbor flower (flowerbed[2] = 1).
            empty_left = False (previous plot has a flower).
            Cannot plant; skip.
            
            Index 4: i = 4, plot has a flower, skip.
            Final Check: After finishing the loop, check if count >= n => 1 >= 2 is False.
            Output: False.
"""
