"""
Ok, so for this problem we have two strings, s1 and s2, the problem is to return True if s2 contains a permutation of the characters in s1. I think for this it would be useful to use a hash table, since we need to store the counts of each of the characters from string 1 in the window we are looking at in string 2. The characters in string 1 can be anything, and can contain any number of repeated characters from each, so we will need to initialize hashmaps with keys that correspond to unique characters from s1, and then we can proceed.
We then need proceed to looking at the second string using a sliding window and 2 pointers to check if we have a permutation, and that's just easy, we will need to see if two dicts are the same.
 """

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
       
        freq = [0]*26

        for val in s1:
            freq[ord(val)%ord('a')] += 1
       
        lp = 0
        rp = len(s1)-1

        while rp < len(s2):
            freq_sub = [0]*26
            for i in range(lp,rp+1,1):
                freq_sub[ord(s2[i]) % ord('a')] += 1
            if freq_sub == freq:
                return True
            lp,rp = lp+1,rp+1
        return False
    


