from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def twoSum(start: int, target: int) -> List[List[int]]:
            res = []
            left, right = start, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return res

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            pairs = twoSum(i + 1, target)
            for pair in pairs:
                result.append([nums[i]] + pair)

        return result
