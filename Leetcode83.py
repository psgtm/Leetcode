class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip the next node since it's a duplicate
                current.next = current.next.next
            else:
                # Move to the next node if it's not a duplicate
                current = current.next
        
        return head