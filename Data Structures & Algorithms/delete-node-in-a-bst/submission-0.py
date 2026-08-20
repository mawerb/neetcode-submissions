# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return root


        if curr.left and curr.right:
            replacement_parent = curr
            replacement = curr.left

            while replacement.right:
                replacement_parent = replacement
                replacement = replacement.right
            
            curr.val = replacement.val
            parent = replacement_parent
            curr = replacement

        child = curr.left if curr.left else curr.right

        if parent is None:
            return child

        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child
        return root
                



