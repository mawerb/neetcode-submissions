# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        while curr:
            prev = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if val < prev.val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root
        