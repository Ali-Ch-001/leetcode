"""
25. Reverse Nodes in k-Group
Difficulty: Hard
https://leetcode.com/problems/reverse-nodes-in-k-group/

──────────────────────────────────────────────────

Given the head of a linked list, reverse the nodes of the list k at a
time, and return the modified list.

k is a positive integer and is less than or equal to the length of
the linked list. If the number of nodes is not a multiple of k then
left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes
themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

 

Constraints:

	• The number of nodes in the list is n.

	• 1 <= k <= n <= 5000

	• 0 <= Node.val <= 1000

 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(next=head)
        group_prev = dummy
        while True:
            node = group_prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            group_next = node.next
            prev, cur = None, group_prev.next
            old_first = group_prev.next
            for _ in range(k):
                cur.next, prev, cur = prev, cur, cur.next
            group_prev.next = prev
            old_first.next = group_next
            group_prev = old_first
