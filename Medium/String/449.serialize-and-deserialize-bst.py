"""
449. Serialize and Deserialize BST
Difficulty: Medium
https://leetcode.com/problems/serialize-and-deserialize-bst/

──────────────────────────────────────────────────

Serialization is converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search
tree. There is no restriction on how your
serialization/deserialization algorithm should work. You need to
ensure that a binary search tree can be serialized to a string, and
this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]

Example 2:

Input: root = []
Output: []

 

Constraints:

	• The number of nodes in the tree is in the range [0, 10^4].

	• 0 <= Node.val <= 10^4

	• The input tree is guaranteed to be a binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        tokens = [int(x) for x in data.split(",")]
        index = 0

        def build(low: float, high: float) -> Optional[TreeNode]:
            nonlocal index
            if index >= len(tokens) or not (low < tokens[index] < high):
                return None
            value = tokens[index]
            index += 1
            node = TreeNode(value)
            node.left = build(low, value)
            node.right = build(value, high)
            return node

        return build(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
