class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows,cols = len(matrix),len(matrix[0])

        def _recur(prev,loc):
            x,y = loc
            if x < 0 or x == rows or y < 0 or y == cols or matrix[x][y] <= prev:
                return 0
            if loc in memo:
                return memo[loc]

            

            

            
            pos_locs = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            res = 1
            previ = matrix[x][y]
            for loca in pos_locs:
                res = max(res, 1 + _recur(previ,loca))
            memo[loc] = res
            return res
            
            

        for row in range(rows):
            for col in range(cols):
                _recur(-1,(row,col))
        return max(memo.values())

# if (row,col) in memo.keys():
#     cur_max = max(cur_max, memo[(row,col)])
# else:
#     pos_locs = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]
#     prev = matrix[row][col]
#     loc_max = 0
#     for loc in pos_locs:
#         loc_max = max(loc_max, 1 + _recur(prev,loc))
#     memo[(row,col)] = loc_max
#     cur_max = max(cur_max,loc_max)