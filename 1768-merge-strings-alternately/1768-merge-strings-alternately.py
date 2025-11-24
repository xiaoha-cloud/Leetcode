class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    # O(n + m)
    # O(n + m)
        result=[]
        l1,l2=0,0
        s1,s2=len(word1),len(word2)
        while l1<s1 and l2<s2:
            result.append(word1[l1])
            l1+=1
            result.append(word2[l2])
            l2+=1
        
        while l1<s1:
            result.append(word1[l1])
            l1+=1
        while l2<s2:
            result.append(word2[l2])
            l2+=1
        
        return "".join(result)
        
        
        