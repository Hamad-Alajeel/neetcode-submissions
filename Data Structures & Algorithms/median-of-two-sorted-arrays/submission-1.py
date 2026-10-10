class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums2)
        n = len(nums1)
        half = (m+n)//2 + 1
        odd = False

        if (m+n)%2 == 1:
            odd = True
        
        
        p1 = -1
        p2 = -1
        count = 0
        last = -1
        cur = -1

        while count < half:
            if ((p2 + 1) >= m and (p1 + 1) < n) or ((p1 + 1) < n and nums1[p1+1] < nums2[p2+1]):
                count += 1
                p1 += 1
                last = cur
                cur = nums1[p1]
            elif (p2 + 1) < m:
                count += 1
                p2 += 1
                last = cur
                cur = nums2[p2]
            else:
                break

        return cur if odd else (cur+last)/2


        