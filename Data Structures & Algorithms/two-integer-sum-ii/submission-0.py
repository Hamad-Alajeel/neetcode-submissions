class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx2 = len(numbers)-1
        idx1 = 0
        while idx1 != idx2:
            cur_sum = numbers[idx1] + numbers[idx2]
            if cur_sum == target:
                return [idx1+1,idx2+1]
            elif cur_sum > target:
                idx2 -= 1
            else:
                idx1 += 1
        return [None,None]