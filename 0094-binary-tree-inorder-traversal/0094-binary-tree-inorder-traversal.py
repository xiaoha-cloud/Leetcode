# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder(node):
            if not node:
                return 
            
            left=inorder(node.left)
            result.append(node.val)
            right=inorder(node.right)
            
        inorder(root)
        return result
        
#    Time: O(n)
#    Space:O(h)