# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Do not return anything, modify node in-place instead.
        """
        nxt = node.next
        node.val = nxt.val
        node.next = nxt.next