# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # research the tree to find the key node
        # handle the subtree 
            # 1. have no child tree  -->delete it -->return Node
            # 2. only on childe tree -->replace ->if not root.right: root.left
            #                                      ->if not root.right: root.left
            # 3. have two child tree --> find the minNode  ->replace the value and delete the node   
            #   3           4          4
            #  2   4      2   4      2

        def findMin(node):
                while  node.left:
                    node=node.left
                return node
            

        #  single node case
        if not root:
            return None
            
        if root.val>key:
            root.left =self.deleteNode(root.left,key)
        elif root.val<key:
            root.right =self.deleteNode(root.right,key)
        else:
            # find it and delete it
            # case 1:
            if not root.left and not root.right:
                return None
                # case 2
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # case 3
            minNode=findMin(root.right)
            root.val= minNode.val
            root.right=self.deleteNode(root.right,minNode.val)
        return root
                
                

        