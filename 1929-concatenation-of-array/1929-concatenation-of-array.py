class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1. use n to record the length of nums, use list as ans
        # 2. for loop to record the element from the nums
        # 3. Time O(N)
        # 4. Space O(N)
        n=len(nums)
        ans=[]

        for i in range(2*n):
            index= i%n
            ans.append(nums[index])
        print(ans)
        return ans

        