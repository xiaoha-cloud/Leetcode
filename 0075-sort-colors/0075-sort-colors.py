class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use two pointer to modify the nums
        # if the current element is 0 then swap with l
        # if the current element is 2 then swap with r
        # O(n） 
        # O(1)

        l,i,r=0,0,len(nums)-1
        while i<= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            else:
                i+=1
        