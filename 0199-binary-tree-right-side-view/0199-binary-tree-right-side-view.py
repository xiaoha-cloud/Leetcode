# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if not root:
                return []
            res=[]
            queue=deque([root])
            while queue:
                size=len(queue)
                for i in range(size):
                    # first in last out 先进后出
                    node = queue.popleft()
                    # 拿到右边的端点
                    if i == size-1:
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res
        return bfs(root)
                
