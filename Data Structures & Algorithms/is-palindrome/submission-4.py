"""
What is the problem? We are given an input string containing words, and we are expected to output a boolean indicating whether there was a palindrome or not in the input string. What are examples we could see here?

Examples:
- "Was it I saw"
- "tab a cat"
- "Hi"


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        
        lp = 0
        rp = size-1
        while lp < rp:
            while not s[lp].isalnum() and lp != rp:
                lp += 1
            while not s[rp].isalnum() and lp != rp:
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            else:
                lp += 1
                rp -= 1
        return True

