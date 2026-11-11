# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head.next
        fast = head.next
        
        if fast is None:
            return False
        fast = fast.next

        while fast and slow:
            if fast is slow:
                return True
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            slow = slow.next

        return False