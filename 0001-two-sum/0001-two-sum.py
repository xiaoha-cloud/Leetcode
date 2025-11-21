class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        record ={}
        for i in range(n):
            if target - nums[i] in record:
                return [record[target - nums[i] ],i]
            else:
                record[nums[i]] = i
    
