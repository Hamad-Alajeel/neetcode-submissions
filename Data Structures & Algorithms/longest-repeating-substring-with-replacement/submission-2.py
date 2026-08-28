"""
What is the problem? We have a string S, consisting of only upper case english letters, and we have an integer k. We are told that we can replace up to k characters in this string with any other uppercase english character. The output is this: the longest substring with one distinct character that can be achieved with k replacements of the original input string. What are examples that we could deal with here?
- "XYYX", k =2, out=4
- "XYYX", k=1, out=3
- "BAAABAB", k=1, out=5
- "ABABABAA"
- "AAABBBA", k=1, out=4
- "AABBBAB", k=2, out = 5

We can use a hash table for this somehow? I am guessing the hash table will keep store of the index of the most recently seen character of a specific upper case characeter? One thing to note about this problem is that we will not be choosing any random upper case letters, we will re-use upper case letters that already exist in the string. Will we require multiple passes? 

Ok, this is my idea: make a first pass and store the frequency of each characeter. For the character containing the most occurrences, make another sweep using pointers with the aim of finding where we can make the replacements that will lead to the highest output value. We can compare this to a binary number of 1's and 0's where we need to find where we can replace 0's with 1's that will lead to the biggest substring of 1's in that string.  
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


        """OLD ATTEMPT"""
        # # Finding character with highest frequncy:
        # freq={}
        # for char in s:
        #     if freq.get(char,0):
        #         freq[char] += 1
        #     else:
        #         freq[char] = 0

        # most_freq = -1
        # most_char = None
        # for char,val in freq.items():
        #     if val >= most_freq:
        #         most_char = char
        #         most_freq = val
        
        #Bad idea that doesn't make sense, what if we have ABBBABA and we have two replacements. We need to find a way to dynamically replace characters in this array. The order of where to place these characters matters: ABBBAABA with k=2? We don't need to do all 2, we can do 0 or even 1. So, this is an optimization with a constraint. If this is a sliding window problem, then we need to pointers in the beginning that do something. One will keep moving forward until it encounters an occurrence of the most_freq character. Then the second pointer needs to do something about that? The sliding window needs to explore the whole array and store something somewhere.
        # largest = -1
        # begin=0
        # end=0
        # size = len(s)
        # while begin < size:
        #     if s[begin] != most_char or s[min(begin+k,size-1)] != most_char:
        #         begin+=1
        #     else:
        #         buff=k
        #         count=1
        #         end=begin+1
        #         while end < size:
        #             if s[end] != most_char and buff > 0:
        #                 buff-=1
        #                 count+=1
        #             elif s[end] != most_char and buff == 0:
        #                 break
        #             elif s[end] == most_char:
        #                 count+=1
        #             end+=1
        #         if count > largest:
        #             largest = count
        #         begin = end
        
        # return largest



                
            



        