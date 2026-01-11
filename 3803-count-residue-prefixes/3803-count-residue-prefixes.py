class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen=[False]*26
        distinct =0
        ans = 0

        for i,ch in enumerate(s,start =1):
            idx= ord(ch)-ord('a')
            if not seen[idx]:
                seen[idx]=True
                distinct +=1
            if distinct == (i%3):
                ans+=1
        return ans
        