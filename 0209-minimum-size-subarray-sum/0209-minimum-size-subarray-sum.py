class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 1. use sliding window to calculate the sum of num in window
        # 2. if the number is greater then start to shrink
        # 3. update the minmum length of the nums
        # 4. O(n) and O(n)
        # 5. edge case if all element is smaller then return 0
        #              if first element is greater then return 1
        minLen= float('inf')
        
        total =0
        l = 0
        for r in range(len(nums)):
            total+=nums[r]

            while total>=target:
                # update the length
                minLen= min(minLen,r-l+1)
                total-=nums[l]
                l+=1
            
            
        return 0 if minLen == float('inf') else minLen
            


        