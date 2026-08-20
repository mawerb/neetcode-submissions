# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast:
            slow = slow.next
            if fast.next == None:
                break
            fast = fast.next.next
        
        stack = []

        while slow:
            stack.append(slow.val)
            slow = slow.next
        
        while stack:
            if (head.val != stack.pop()):
                return False
            head = head.next

        return True