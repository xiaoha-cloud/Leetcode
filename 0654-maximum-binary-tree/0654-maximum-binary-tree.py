# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# build function to separte the nums
# in the build function check the max_value and take out the max_index 
# build the tree node and build the left or right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(l,r):
            if l>r:
                return None

            max_index=l
            for i in range(l+1,r+1):
                if nums[i]>nums[max_index]:
                    max_index=i
            root = TreeNode(nums[max_index])
            root.left=build(l,max_index-1)
            root.right=build(max_index+1,r)
            return root
        return build(0,len(nums)-1)
        