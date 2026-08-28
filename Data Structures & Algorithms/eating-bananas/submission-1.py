class Solution:
    def time_taken(self,k,piles):
        time = 0
        for pile in piles:
            time += math.ceil(pile/k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        min_bananas = 1
        k = (max_bananas + min_bananas)//2
        while max_bananas >= min_bananas :
            
            time = self.time_taken(k,piles)
            if time <= h:
                max_bananas = k - 1
                k = (max_bananas + min_bananas)//2
            elif time > h:
                min_bananas = k + 1
                k = (max_bananas + min_bananas)//2
        return min_bananas