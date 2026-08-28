# we have an array of integers, and we have a target number. We want to return the distinct indicies of two elements from the array that add up to the target. What is the brute force solution: checking every combination of 2 elements from the array until we get the value of target. this is O(n^2) which is very big time complexity and the space complexity is O(1).
# So, what is the smarter solution to this? 
# Firstly, whatever numbers are chosen to add to the target need to be lower than or equal to the target number. I would use pointers for this problem, but I don't think that it is relevant. Recommeneded space complexity is O(n), so I am thinking we will need to store a sorted array for this. and then use pointers? I feel like we need 
# Indicies need to be seperate, so which index 
# Can I rearrange the equation to fix and index which may be any index for me to iterate on? 
# target - nums[j] == nums[i], so fix on one index and iterate over the others that don't equal it
# [1,2,3] 3//2 = 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,fixed_val in enumerate(nums):
            for j,mov_val in enumerate(nums):
                if i!=j and target-fixed_val==mov_val:
                    return sorted([i,j])
        return None