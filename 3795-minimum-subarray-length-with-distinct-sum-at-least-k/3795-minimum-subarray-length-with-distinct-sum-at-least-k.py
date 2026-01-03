class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        drelanvixo = nums
        freq = defaultdict(int)
        distinct_sum = 0
        

        
        l=0
        window_sum = 0
        ans = float("inf")

        for r,x in enumerate(drelanvixo):
            if freq[x] == 0:
                distinct_sum += x
            freq[x]+=1
            
            while distinct_sum >= k and l <= r: 
                ans = min(ans, r-l+1)

                y = drelanvixo[l]
                freq[y] -= 1
                if  freq[y] == 0:
                    distinct_sum -= y 
                l+=1
                
            
                
                
        return  -1 if ans == float("inf") else ans
        
        