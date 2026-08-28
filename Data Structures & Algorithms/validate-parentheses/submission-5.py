class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}":"{",")":"(","]":"["}
        stack = []

        for char in s:
            if (char == "}" or char == "]" or char ==")") and stack and close_to_open[char] == stack[-1]:
                stack.pop()
            elif (char == "}" or char == "]" or char ==")") and stack and close_to_open[char] != stack[-1]:
                return False
            else:
                stack.append(char)

        return True if not stack else False

