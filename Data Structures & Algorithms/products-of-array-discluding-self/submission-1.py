"""
I have an input array called nums which contains integers. The output array of this method is an array of similar size to the input array. Each element of the output array represents the product of all the elements in the input array except that located at the index of the element we are looking at in the output array. 

What are example inputs we could be dealing with:
- generic: [1, 2, 3]
- one zero: [0, 1, 1]
- > one zero: [0,1,0]
- negatives (I think this isn't that big of a deal)

What could be a brute force solution to this problem? Depending on which amount of zeros there are in the input array, we could use the product of the elements in the input array to determin the values of the elements in the output array.
1- no zeros: just use the product/nums[i] for each i
2- one zero: find product of non-zero elements and place that at the index where nums has a 0.
3- > one zeros: return all 0's

To find the amount of 0's we first need to sweep the array using a pointer that counts how many 0's are there. It can stop after counting 2.
"""


import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        size = len(nums)
        output = [0]*size
        idx_zero = None
        prod_all = 1

        for i,val in enumerate(nums):
            if val == 0:
                zeros += 1
                idx_zero = i
            else:
                prod_all *= val

            if zeros == 2:
                prod_all = 0
                break
        
        if zeros == 2:
            return output

        elif zeros == 1:
            output[idx_zero] = prod_all
            return output
        
        else:
            
            for i,val in enumerate(nums):
                output[i] = prod_all//val
            return output




        