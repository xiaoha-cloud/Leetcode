class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case
        n = len(nums)
        if n == 0:
            return 
        # handle the k
        if k >= n:
            k %=n
            if k == 0:
                return 
        # orginal:      [1 2 3 4 5 6 7 8]
        # reverse the whole:  [8 7 6 5 4 3 2 1]
        # front k=4:    [5 6 7 8 | 4 3 2 1]
        # back n-k:    [5 6 7 8 | 1 2 3 4]  

        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        

       