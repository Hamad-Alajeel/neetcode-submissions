class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}
        
        for char1,char2 in zip(s,t):
            if char1 in dict_s.keys():
                dict_s[char1] += 1
            else:
                dict_s[char1] = 1

            if char2 in dict_t.keys():
                dict_t[char2] += 1
            else:
                dict_t[char2] = 1

        for key,val in dict_s.items():
            if not dict_t.get(key) or dict_t.get(key) != val:
                return False

        return True