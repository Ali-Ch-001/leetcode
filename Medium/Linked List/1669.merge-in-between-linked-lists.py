"""
1669. Merge In Between Linked Lists
Difficulty: Medium
https://leetcode.com/problems/merge-in-between-linked-lists/

──────────────────────────────────────────────────

You are given two linked lists: list1 and list2 of sizes n and m
respectively.

Remove list1's nodes from the a^th node to the b^th node, and put
list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.

 

Example 1:

Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 =
[1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in
their place. The blue edges and nodes in the above figure indicate the
result.

Example 2:

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 =
[1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate
the result.

 

Constraints:

	• 3 <= list1.length <= 10^4

	• 1 <= a <= b < list1.length - 1

	• 1 <= list2.length <= 10^4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        for _ in range(a - 1):
            prev = prev.next
        after = prev
        for _ in range(b - a + 1):
            after = after.next
        after = after.next
        prev.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after
        return list1
