class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 1. This is a fix window and use the window to capture the vowels number.
        # 2. initialze the window l result window
        # 3. iterate the array or string
        # 4. update the window 
        # 5.  while the window is out of the boundary?
        # 6. shrink the window
        # 7. update the result
        l=0
        result=0
        vowel=0

        for r in range(len(s)):
            if s[r] in 'aeiou':
                vowel+=1

            while r-l+1>k:
                if s[l] in 'aeiou':
                    vowel-=1
                l+=1
            if r-l+1==k:
                result=max(result,vowel)
            
        return result

# T:O(n)
# S:O(1)
        