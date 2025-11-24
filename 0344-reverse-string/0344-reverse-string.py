class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # O（n）
        # O(1）
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            r-=1
            l+=1
        