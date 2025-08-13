class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        char=set()
        l=0
        # use the sliding window (by using set() )to calculate the charaters
        # each time update the maximum length
        for r in range(len(s)):
            # if the cha is already inside the set then remove it update the left index
            while s[r] in char:
                char.remove(s[l])
                l+=1

            # the cha is not in the set so add it in the set
            char.add(s[r])
            max_length=max(max_length,r-l+1)
        return max_length

    
        # Time complexity O(n)
        # Space complexity:O(n)