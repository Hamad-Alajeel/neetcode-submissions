class Solution:
    def searchList(self, list: List[int], target: int) -> int:
        left = 0
        right = len(list) - 1
        while left <= right:
            mid = (left + right)//2
            val = list[mid]
            if val == target:
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end = len(matrix) - 1
        begin = 0
        while begin <= end:
            mid = (begin + end) // 2
            first_val = matrix[mid][0]
            if first_val == target:
                return True
            elif first_val > target:
                end = mid - 1
            else:
                begin = mid + 1

        if begin <= len(matrix) - 1:
            begin_first_val = matrix[begin][0]
        else:
            begin_first_val = target + 1
            
        end_first_val = matrix[end][0]

        if begin_first_val < target:
            return self.searchList(matrix[begin],target)
        elif end_first_val < target:
            return self.searchList(matrix[end],target)
        else:
            return False