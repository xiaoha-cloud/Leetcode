class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # 1. locate the need to reverse area
        # 2. swap the area  abcd k=4 d c b a
        # edge case:
           #  1. empty " "  k =1 : return  ""
           #  2. single  h  k = 1  : return 
           #  3.            k > len(s)  to see what is left
        if len(s)==0:
            return s
        
        if k> len(s):
            k %=len(s)
        
        l,r=0,k-1

        arr = list(s)
        while l<= r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
        return "".join(arr)
        