class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # initialize the l result window
        # go throught the array
        # update the result
        # while out of the boundary shrink the window
        # return the result
        # O(n）T
        # O(1) S
        win_sum=sum(nums[:k])
        best=win_sum
        for r in range(k,len(nums)):
            win_sum += nums[r] - nums[r-k]
            best = max(best,win_sum)
        return best/k