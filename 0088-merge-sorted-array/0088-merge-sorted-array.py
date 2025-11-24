class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
         # "Besides the core logic, I also considered several edge cases to ensure the solution is robust. Let me walk through them briefly.
        # from the right to add the elements

        p1,p2=m-1,n-1
        p=m+n-1

        while p1>= 0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1
        
        while p2>=0:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1
    # By considering these edge cases, I make sure the algorithm not only works for the average case but also performs correctly under boundary and extreme inputs, which is essential in real-world systems.
    #case 1:    nums1 = [0], m = 0; nums2 = [1], n = 1  copy the nums2 to nums1
    #case 2:    nums1 = [1], m = 1; nums2 = [],  n = 0  unchange 
    #case 3:    nums1 = [1,1,1,0,0,0], m = 3; nums2 = [1,1,1], n = 3  
    #      Even though values are identical, the algorithm still needs to preserve all elements in sorted order.

    #case 4:    nums1 = [4,5,6,0,0,0], m = 3; nums2 = [1,2,3], n = 3
    # Since all elements in nums2 are smaller than the ones in nums1, the merged result should be nums1 = [1,2,3,4,5,6] 
    # So the algorithm must shift all nums1 elements to the right to make space.

    #case 5:    nums1 = [1,2,3,0,0,0], m = 3; nums2 = [4,5,6], n = 3
    # Just need to copy nums2 into the remaining slots.
        