import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a min-heap
        min_heap = []
        
        # Add the first node of each list to the heap (if it's not empty)
        for idx, l in enumerate(lists):
            if l:
                # Push a tuple (node's value, index of the list, node itself) into the heap
                heapq.heappush(min_heap, (l.val, idx, l))
        
        # Create a dummy head to build the result list
        dummy = ListNode()
        current = dummy
        
        # Process the heap until it's empty
        while min_heap:
            # Extract the node with the smallest value
            val, idx, smallest_node = heapq.heappop(min_heap)
            # Add it to the result list
            current.next = smallest_node
            current = current.next
            
            # If there is a next node, push it to the heap
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, idx, smallest_node.next))
        
        # The dummy's next points to the head of the merged list
        return dummy.next
