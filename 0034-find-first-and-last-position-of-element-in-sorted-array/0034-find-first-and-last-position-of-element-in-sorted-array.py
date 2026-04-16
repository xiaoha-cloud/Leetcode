class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # in non-decreasing order 
        # record the first and then check the rest on use (l,r)
        # use a boolen to make sure if we want to continue search
        def binary(nums,target,is_searching_left):
            l,r=0,len(nums)-1
            idx=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    idx=mid
                    # continue to search the left
                    if is_searching_left:
                        r=mid-1
                    else:
                        l=mid+1
            return idx
        
        left = binary(nums,target,True)
        right= binary(nums,target,False)
        return [left,right]
        