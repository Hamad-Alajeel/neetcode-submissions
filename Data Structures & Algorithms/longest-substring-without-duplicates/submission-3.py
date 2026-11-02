class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seq = set()
        l,r = 0,0

        while r < len(s):
            if l==r:
                seq.update(s[l])
                if len(seq) > longest:
                    longest = len(seq)
                r+=1
            elif s[r] not in seq:
                seq.update(s[r])
                if len(seq) > longest:
                    longest = len(seq)
                r+=1
            else:
                while s[r] in seq:
                    l += 1
                    seq.remove(s[l-1])
                
            
        return longest

