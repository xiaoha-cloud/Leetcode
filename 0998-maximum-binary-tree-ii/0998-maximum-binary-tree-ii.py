# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,val):
            if root is None:
                return  TreeNode(val)
        
            if val>root.val:
                new_root=TreeNode(val)
                new_root.left=root
                return new_root
            
            root.right=insert(root.right,val)
            return root
        
        return insert(root,val)