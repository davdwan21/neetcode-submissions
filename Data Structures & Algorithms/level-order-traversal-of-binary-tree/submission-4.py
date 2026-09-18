# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            level_vals = []
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                level_vals.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            ans.append(level_vals)

        return ans

# start at root
# if root is empty, return empty
# else, keep track of a number i
# i = 1, every iteration i * 2
# initialize a pointer at 0
# put from p to p + i in an array
# append that to res
# idk what im doing