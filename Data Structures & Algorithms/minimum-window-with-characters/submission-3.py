"""
I remember I was reading about this problem in the book I was reading. I need to go through the string we are comparing to first, and then I need to go through the second string continuosly incrementing and decrementing as I move with the minimum window. In a window problem like this, I need two pointers that point to different indicies representing the left and right sides of a window I am using. I need the smallest substring that contains all the characters from the original string, so the smallest substring may be the whole of string s or a part of it that contains other characters or nothing if s and t are completely different and do not contain intersecting characters. For this what data structure should I use? Definitely a hashmap because I want to keep track of the counts of the values of each character. For that I feel like using a list. I will use a list. The list stores the number of each character from t. the list will be size 26 and I will use the ord function to index the list correctly. I will also keep count of the length of string t while I am moving. I will keep moving until the count of characters left that need to be covered by the substring in s go to 0, then I will move the left pointer forward until the count goes up by 0 again. Hmmm actually, I just realized something I need to return the substring itself, not the length of the minimum substring.

Knowing that I have to return the actual substring instead of the size of that substring, how does my solution change? I need to initialize an initial shortest substring which should just be []. Then once I have completed one cycle of moving the right and left pointers I can then compare the size

"""


class Solution:
    # def _alph_index(self, s: str) -> int:
    #     # Used to correctly choose the right index
    #     assert len(s) == 1

    #     num = ord(s)
        
    #     if num < 97:
    #         index = num - 65
    #     else:
    #         index = num - 97 + 26

    #     return index

    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        # First initialize alphabet hash using string t:
        freq_t, window = {}, {}
        

        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
        
        need = len(freq_t)
            
        
        # now we have both the size of t and a hashmap with the number of each unique char
        # it possess. 
        # We now initialize an empty list that is supposed to contain the shortest substring and pointers. At each iteration of our loop we will re-initialize a new sub_string to compare it to the previous shortest. At each iteration, we add +1 to the right pointer. we always need to append the characters to sub_string to be able to return it at the end. 
        l = 0
        min_res = float("inf")
        res = (-1,-1)
        have = 0

        for r in range(len(s)):

            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in freq_t and window[char] == freq_t[char]:
                have += 1
            
            # the logic for moving the left pointer will be here
            while have == need:
                # upadte our result
                if (r - l + 1) < min_res:
                    min_res = r - l + 1
                    res = (l, r + 1)
                # pop from the left of the window
                window[s[l]] -= 1
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1


        l,r = res
        return s[l:r] if min_res != float("inf") else ""

            
        








