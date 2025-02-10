from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the 2nd list
        cur = slow.next
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            head2 = cur
            cur = next
        
        node1 = head
        node2 = head2
        while node1 and node2:
            next1 = node1.next
            node1.next = node2
            next2 = node2.next
            node2.next = next1
            node1 = next1
            node2 = next2
   


