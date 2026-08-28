# We have a 9x9 board. Every column must not contain a duplicate of the numbers 1-9, every row must not contain a duplicate of the numbers 1-9. Every column must not contain a duplicate of the numbers 1-9. Boexes may be empty and only contain a ".". They do not count. The output is a bool that indicates whether a board is valid or not.
# What is the brute force solution?
"""
- iterate through all the rows and check if there are duplicates
- iterate through all columbns and do the same
- iterate through all boxes and check if they are the same
This is a O(n^2) solution.

How can I use a hashmap for this problem? To check for duplicates, ignoring "."

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First iterate through rows to check for duplicates:
        for i in range(9):
            row_hash = {}
            for num in board[i]:
                if num not in row_hash and num != ".":
                    row_hash[num] = 1
                elif num == ".": 
                    continue
                else:
                    return False
        
        # Now we iterate through columns:
        for i in range(9):
            col_hash = {}
            for j in range(9):
                cur_num = board[j][i]
                if cur_num not in col_hash and cur_num != ".":
                    col_hash[cur_num] = 1
                elif cur_num == ".":
                    continue
                else:
                    return False
        
        # now we iterate through grids that are 3x3
        # how do we do this? 
        # There is a way to dynamically store the values in the correct hash map.
        # There technically needs to be 9 of them. 
        grid_hash = {(i,j):dict() for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                cur_num = board[i][j]
                if cur_num not in grid_hash[(i//3,j//3)] and cur_num != ".":
                    grid_hash[(i//3,j//3)][cur_num] = 1
                elif cur_num == ".":
                    continue
                else:
                    return False

        # End
        return True

        