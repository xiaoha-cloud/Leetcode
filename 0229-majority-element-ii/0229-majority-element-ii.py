class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # O(n)
        # O(n)
        res=set()
        n=len(nums)
        counter={}

        for i in range(n):
            counter[nums[i]]= counter.get(nums[i],0)+1
            if counter[nums[i]]> (n/3):
                res.add(nums[i])
        return list(res)
