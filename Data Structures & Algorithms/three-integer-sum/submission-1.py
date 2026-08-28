class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums)
        triplets = []
        nums.sort()

        for i,val in enumerate(nums):
            lp = 0
            rp = size-1
            target = -val
            while lp!=rp and lp != size and rp != -1:
                if nums[lp] + nums[rp] < target:
                    lp += 1
                elif nums[lp] + nums[rp] > target:
                    rp -= 1
                else:
                    triplet = sorted([nums[lp],nums[rp],nums[i]])
                    if triplet not in triplets and lp != i and rp != i:
                        triplets.append(triplet)
                    lp += 1
                    rp -= 1

        return triplets 

