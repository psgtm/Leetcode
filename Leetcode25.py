# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list
        def reverseLinkedList(head, k):
            prev, curr = None, head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        # Dummy node to simplify the edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            # Reverse the k nodes
            group_next = kth.next
            # Reverse this group
            prev, curr = group_prev.next, group_prev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Adjust the pointers
            temp = group_prev.next
            group_prev.next = kth
            temp.next = group_next
            
            # Move the group_prev to the end of the reversed group
            group_prev = temp