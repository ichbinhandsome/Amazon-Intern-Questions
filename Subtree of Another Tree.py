'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, s, t):
        if not s and not t: return True
        if (not s and t) or (not t and s) or (s.val != t.val):
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def pre_order(node, t):
            if not node: return False
            return self.check(node, t) or pre_order(node.left, t) or pre_order(node.right, t)
        return pre_order(s, t)
############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSametree(self, s, t):
        if not s and not t: return True
        if (not s and t) or (not t and s) or (s .val != t.val):
            return False
        return self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
            
        