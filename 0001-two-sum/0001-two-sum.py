class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(len(nums)):
            if target - nums[i] in index:
                return [i,index.get(target - nums[i])]
            index[nums[i]]=i

        # Time Complexity: O(n)
        # Space Complexity:O(N)