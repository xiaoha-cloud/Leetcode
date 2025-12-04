class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
                # O(n)
        # O(1)
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0]
            for s in strs[1:]:
                if i>= len(s) or s[i]!=char[i]:
                    return char[:i]
        return strs[0]