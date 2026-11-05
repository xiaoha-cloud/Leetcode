class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # initialize the l result window
        # go throught the array
        # update the result
        # while out of the boundary shrink the window
        # return the result
        # O(n）T
        # O(1) S
        l=0
        win_sum=0
        result=float('-inf')

        for r in range(len(nums)):
            win_sum+=nums[r]
            while r-l+1>k:
                win_sum-=nums[l]
                l+=1
            if r-l+1==k:
                result=max(result,win_sum)
        return result/k
