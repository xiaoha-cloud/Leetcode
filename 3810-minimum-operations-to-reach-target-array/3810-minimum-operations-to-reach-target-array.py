class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        need =set()
        for a,b in zip(nums,target):
            if a!=b:
                need.add(a)
        return len(need)