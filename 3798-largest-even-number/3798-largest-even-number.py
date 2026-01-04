class Solution:
    def largestEven(self, s: str) -> str:
        # 1. totally no 2
        # 2. end with 2 return s
        # 3. end with 1 return the last index of 2
        if not "2" in s:
            return ""
        
        if s[-1] == "2":
            return s
        
        last_2_index = s.rfind("2")
        return s[:last_2_index+1]
        