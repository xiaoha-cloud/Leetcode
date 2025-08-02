class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # edge case:
        # 1.if length of p >length of s
        if len(p)>len(s):
            return []
        # Method
        # 1.import the Counter
        p_count=Counter(p)
        s_count={}
        result=[]
        # Initialize window
        for i in range(len(p)):
            s_count[s[i]]=s_count.get(s[i],0)+1
        if s_count==p_count:
            result.append(0)

        for i in range(len(p),len(s)):
            char=s[i]
            s_count[char]=s_count.get(char,0)+1

            # remove the previous one
            old_char=s[i-len(p)]
            s_count[old_char]-=1
            if s_count[old_char]==0:
                del s_count[old_char]
            
            if s_count==p_count:
                result.append(i-len(p)+1)
        return result

# T:O(n)
# S:O(n)