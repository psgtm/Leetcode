# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers, both starting at the dummy node
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead to maintain the gap
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first one reaches the end of the list
        while first:
            first = first.next
            second = second.next
        
        # The second pointer is now right before the node to be removed
        second.next = second.next.next
        
        # Return the new head of the list
        return dummy.next
