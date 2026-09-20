# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of our result list
        # This simplifies edge cases where the list is empty initially
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop continues if there are nodes in l1, l2, or a remaining carry
        while l1 or l2 or carry:
            # Get values safely (use 0 if the node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total and new carry
            total = val1 + val2 + carry
            carry = total // 10      # Integer division to get the carry (e.g., 15 // 10 = 1)
            new_digit = total % 10   # Modulus to get the single digit (e.g., 15 % 10 = 5)
            
            # Create a new node with the calculated digit and attach it
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move input pointers forward if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the next node after dummy (the actual head of the result)
        return dummy.next