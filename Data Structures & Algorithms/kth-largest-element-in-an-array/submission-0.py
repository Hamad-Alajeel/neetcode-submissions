class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        out = 0
        for i in range(k):
            out = heapq.heappop(maxHeap)
        return -out
