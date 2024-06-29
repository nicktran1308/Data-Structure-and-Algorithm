"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            newMax = max(rightMax, temp)
            arr[i] = rightMax
            rightMax = newMax
        return arr


"""
Time Complexity: O(n) - n : number of elements in the array, only pass through the array once
Space Complexity: O(1) - no extra space is used

Steps:

    len(arr) - 1 is the index of the last element in the array
    '-1'  stopping point of the loop, loop continue to go down after 0, stop at -1 to make sure it include 0
    '-1' loop counts backwards from len(arr) - 1 to 0

    arr = [17,18,5,4,6,1]
    temp = arr[5] = 1
    newMax = max(rightMax, temp) = max(-1, 1) = 1
    arr[5] = rightMax = -1
    rightMax = newMax = 1

    temp = arr[4] = 6
    newMax = max(rightMax, temp) = max(1, 6) = 6
    arr[4] = rightMax = 1
    rightMax = newMax = 6

    temp = arr[3] = 4
    newMax = max(rightMax, temp) = max(6, 4) = 6
    arr[3] = rightMax = 6
    rightMax = newMax = 6

    temp = arr[2] = 5
    newMax = max(rightMax, temp) = max(6, 5) = 6
    arr[2] = rightMax = 6
    rightMax = newMax = 6

    temp = arr[1] = 18
    newMax = max(rightMax, temp) = max(6, 18) = 18
    arr[1] = rightMax = 6
    rightMax = newMax = 18

    temp = arr[0] = 17
    newMax = max(rightMax, temp) = max(18, 17) = 18
    arr[0] = rightMax = 18
    rightMax = newMax = 18


"""
