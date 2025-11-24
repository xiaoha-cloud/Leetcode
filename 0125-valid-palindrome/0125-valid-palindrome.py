class Solution:
    def isPalindrome(self, s: str) -> bool:
         # lower() and isalnum()
        # Space 
        # O(n)
        # O(n)

        s = "".join(cha.lower() for cha in s if cha.isalnum())
        print(s)
        l,r=0,len(s)-1
        while l<r: 
            print(s[l],s[r]) 
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    