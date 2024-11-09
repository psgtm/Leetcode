# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the list and skip nodes with the target value
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Remove the node
            else:
                current = current.next  # Move to the next node if no removal
        
        return dummy.next  # Return the new head of the list
