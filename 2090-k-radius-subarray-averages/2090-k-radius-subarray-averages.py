class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        # Array to capture the result all of them are -1
        # if the left size is not enough for the result
        # i-k<=0 : arr[i]=-1
        # i+k>len(nums):arr[i]=-1
        # inside it start to sum and calculate the average

        # if the right size is not enough for the result
        n = len(nums)
        size = 2 * k + 1
        ans = [-1] * n
        if size > n:                    
            return ans

        win_sum = sum(nums[:size])       
        ans[k] = win_sum // size

        for r in range(size, n):
            win_sum += nums[r] - nums[r - size]   
            ans[r - k] = win_sum // size
        return ans