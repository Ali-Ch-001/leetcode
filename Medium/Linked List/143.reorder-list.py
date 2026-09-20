"""
143. Reorder List
Difficulty: Medium
https://leetcode.com/problems/reorder-list/

──────────────────────────────────────────────────

You are given the head of a singly linked-list. The list can be
represented as:

L0 &rarr; L1 &rarr; &hellip; &rarr; Ln - 1 &rarr; Ln

Reorder the list to be on the following form:

L0 &rarr; Ln &rarr; L1 &rarr; Ln - 1 &rarr; L2 &rarr; Ln - 2 &rarr;
&hellip;

You may not modify the values in the list's nodes. Only nodes
themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 

Constraints:

	• The number of nodes in the list is in the range [1, 5 * 10^4].

	• 1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        node = slow.next
        slow.next = None
        while node:
            node.next, prev, node = prev, node, node.next
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
