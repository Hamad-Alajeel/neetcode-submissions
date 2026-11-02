class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        days = [0] * len(temperatures)
        p = 1
        while p < len(temperatures):
            cur_temp = temperatures[p]
            if cur_temp <= stack[-1][0]:
                stack.append((cur_temp,p))
            else:
                while len(stack) > 0 and cur_temp > stack[-1][0]:
                    last = stack.pop()
                    days[last[1]] = p - last[1]
                stack.append((cur_temp,p))
            p += 1
        return days




