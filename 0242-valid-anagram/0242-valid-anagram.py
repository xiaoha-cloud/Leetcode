class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use 1 counter
        # optimize: once we have the counter for s then when
        # we try to take out the cha from the t we delete it until 
        #  leave nothing

        # O(n)
        # O(n)

        # edge case 1: if the length is different
        # edge case 2: if the s and t is null we return True
        #               "" and "" → True

        s_len=len(s)
        t_len=len(t)
        if s_len!=t_len:
            return False
        


        s_counter={}
        for cha in s:
            s_counter[cha]=s_counter.get(cha,0)+1
        
        for cha in t:
            if cha not in s_counter:
                return False
            s_counter[cha]-=1
            if s_counter[cha] < 0:
                return False
                
        return True
                