# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = [(float('-inf'),float('inf'), root)]

        while queue:
            lb, up, curr = queue.pop()

            if curr.left:
                if curr.left.val < curr.val and lb < curr.left.val < up:
                    queue.append((lb, curr.val, curr.left))
                else:
                    return False

            if curr.right:
                if curr.right.val > curr.val and lb < curr.right.val < up:
                    queue.append((curr.val, up, curr.right))
                else:
                    return False

        return True