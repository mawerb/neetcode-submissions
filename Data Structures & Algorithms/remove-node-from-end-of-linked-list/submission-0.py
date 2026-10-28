# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        length -= n
        index = 0
        prev = None
        curr = head

        while index <= length - 1:
            prev = curr
            curr = curr.next
            index += 1

        if curr == head:
            return head.next
        
        prev.next = curr.next

        return head