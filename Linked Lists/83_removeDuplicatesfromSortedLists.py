# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Remove all duplicates from a sorted linked list such that 
        each element appears only once and return the modified list."""
      
        # Initialize current to point to the head of the list
        current = head
      
        # Traverse the linked list
        while current and current.next_node:
            # If the current value is equal to the value in the next node
            if current.value == current.next_node.value:
                # Bypass the next node as it's a duplicate
                current.next_node = current.next_node.next_node
            else:
                # Move to the next unique value if no duplicate is found
                current = current.next_node
              
        # Return the head of the updated list
        return head