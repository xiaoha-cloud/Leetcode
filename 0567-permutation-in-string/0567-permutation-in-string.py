from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # edge case : 1. empty and single return false
        #             2. len(s1) > len(s2 ) return false
        # O(n)
        # O(1)
        if len(s1)>len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:len(s1)])

        if need == window:
            return True
        
        l=0
        for r in range(len(s1),len(s2)):
            window[s2[r]]+=1
            window[s2[l]]-=1
            if window[s2[l]]==0:
                del window[s2[l]]
            l+=1
            if need == window:
                return True
        
        return False
