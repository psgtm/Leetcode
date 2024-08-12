# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to keep track of the head of the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None:
            # Get the current values; if the node is None, use 0
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Set the next node in the result list
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's any carry left at the end, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next of dummy head which is the actual head of the resultant list
        return dummy_head.next
