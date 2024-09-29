# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # Initialize two pointers
        pA = headA
        pB = headB
        
        # Traverse both lists
        while pA != pB:
            # If pointer A reaches the end, switch to head of B
            pA = pA.next if pA else headB
            # If pointer B reaches the end, switch to head of A
            pB = pB.next if pB else headA
        
        # Either they meet at the intersection node or at None
        return pA
