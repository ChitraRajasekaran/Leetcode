# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one element it is already sorted.
        if head is None or head.next_node is None:
            return head

        # Find the middle of the list to split the list into two halves.
        slow, fast = head, head.next_node
        while fast and fast.next_node:
            slow, fast = slow.next_node, fast.next_node.next_node
      
        # Split the list into two halves.
        temp = slow.next_node
        slow.next_node = None
        left_half, right_half = self.sortList(head), self.sortList(temp)
      
        # Merge the two sorted halves.
        dummy_node = ListNode()
        current = dummy_node
        while left_half and right_half:
            # Compare the current elements of both halves and attach the smaller one to the result.
            if left_half.value <= right_half.value:
                current.next_node = left_half
                left_half = left_half.next_node
            else:
                current.next_node = right_half
                right_half = right_half.next_node
            current = current.next_node
      
        # Attach the remaining elements, if any, from either half.
        current.next_node = left_half or right_half
      
        # Return the head of the sorted list.
        return dummy_node.next_node
