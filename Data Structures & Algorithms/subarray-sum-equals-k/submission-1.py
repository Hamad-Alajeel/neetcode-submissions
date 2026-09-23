class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1 if nums[0] == k else 0
        # # brute force: check all the subarrays to see if they sum up to k when they do increment counter by 1
        # count = 0
        # # for i in range(len(nums)):
        # #     cur_sum = nums[i]
        # #     if cur_sum == k:
        # #         count += 1
        # #     for j in range(i+1,len(nums),1):
        # #         cur_sum += nums[j]
        # #         if cur_sum == k:
        # #             count += 1
        # i = 0
        # j = 0
        # cur_sum = 0
        # while i < len(nums):
        #     cur_sum += nums[i]
        #     if cur_sum == k:
        #         j = i + 1
        #         count += 1
        #         while j < len(nums) and j + 1 < len(nums):
        #             if nums[j] == -nums[j+1]:
        #                 count += 1
        #                 j += 2
        #             else:
        #                 break
        #         cur_sum = 0
        #     i += 1
        # return count
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0

        prefSum = {0:1}
        i = 0
        sum = 0
        res = 0
        while i < len(nums):
            sum += nums[i]
            target = sum - k
            exists = prefSum.get(target, None)
            if exists:
                res += exists
            i += 1
            prefSum[sum] = prefSum.get(sum,0) + 1
        return res
            



