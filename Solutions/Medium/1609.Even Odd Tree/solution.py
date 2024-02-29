from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        level = 0
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (
                        previous is not None and node.val <= previous
                    ):
                        return False
                else:
                    if node.val % 2 == 1 or (
                        previous is not None and node.val >= previous
                    ):
                        return False

                previous = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True