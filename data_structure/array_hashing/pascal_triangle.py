"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        # Initialize the first row of the Pascal's triangle
        triangle = [[1]]

        for row_number in range(1, numRows):
            prev_row = triangle[row_number - 1]
            # Start the current row with 1
            current_row = [1]

            # Compute the values in the middle of the row
            for j in range(1, row_number):
                current_row.append(prev_row[j - 1] + prev_row[j])

            # End the current row with 1
            current_row.append(1)

            # Append the current row to the triangle
            triangle.append(current_row)

        return triangle


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)

Steps:
    1. Base Case
    2. Initialize the first row of the Pascal's triangle  [[1]]
    3. Loop through from 1 to numRows
    4. Each new row starts with 1 & ends with 1.
    5. Start the current row with 1
    6. Compute the values in the middle of the row
    7. End the current row with 1

Iteration 1 (row_number = 1):

    prev_row = [1] (the last row in the triangle).
    current_row starts with [1].
    There are no middle elements because the previous row has only one element.
    current_row ends with [1] → current_row = [1, 1].
    Append current_row to triangle → triangle = [[1], [1, 1]].


Iteration 2 (row_number = 2):

    prev_row = [1, 1].
    current_row starts with [1].
    Add the middle elements by summing adjacent elements in prev_row:
    prev_row[0] + prev_row[1] = 1 + 1 = 2 → current_row = [1, 2].
    current_row ends with [1] → current_row = [1, 2, 1].
    Append current_row to triangle → triangle = [[1], [1, 1], [1, 2, 1]].


Iteration 3 (row_number = 3):

    prev_row = [1, 2, 1].
    current_row starts with [1].
    Add the middle elements:
    prev_row[0] + prev_row[1] = 1 + 2 = 3 → current_row = [1, 3].
    prev_row[1] + prev_row[2] = 2 + 1 = 3 → current_row = [1, 3, 3].
    current_row ends with [1] → current_row = [1, 3, 3, 1].
    Append current_row to triangle → triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]].


Iteration 4 (row_number = 4):

    prev_row = [1, 3, 3, 1].
    current_row starts with [1].
    Add the middle elements:
    prev_row[0] + prev_row[1] = 1 + 3 = 4 → current_row = [1, 4].
    prev_row[1] + prev_row[2] = 3 + 3 = 6 → current_row = [1, 4, 6].
    prev_row[2] + prev_row[3] = 3 + 1 = 4 → current_row = [1, 4, 6, 4].
    current_row ends with [1] → current_row = [1, 4, 6, 4, 1].
    Append current_row to triangle → triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]].

"""
