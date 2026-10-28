# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        l_list = []
        curr = head

        while curr:
            l_list.append(curr)
            curr = curr.next

        l = 0
        r = len(l_list) - 1

        prev = None
        while l < r:
            l_list[l].next = l_list[r]
            l += 1

            if l == r:
                break

            l_list[r].next = l_list[l]
            r -= 1

        l_list[l].next = None