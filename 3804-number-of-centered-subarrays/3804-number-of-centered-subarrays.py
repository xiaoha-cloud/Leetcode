class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
       
        n = len(nums)
        ans = 0
        for l in range(n):
            seen = set()
            running_sum = 0
            for r in range(l,n):
                running_sum +=nums[r]
                seen.add(nums[r])
                if running_sum in seen:
                    ans+=1
        return ans
        