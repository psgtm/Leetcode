# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if less than two nodes, no need to swap
        if not head or not head.next:
            return head
        
        # Nodes to be swapped
        first = head
        second = head.next
        
        # Recursively call for the rest of the list
        first.next = self.swapPairs(second.next)
        
        # Swap the two nodes
        second.next = first
        
        # Return the new head node (which is second node after the swap)
        return second
