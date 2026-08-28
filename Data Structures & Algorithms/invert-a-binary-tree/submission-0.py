# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # We need to iterate through the first tree in a depth first manner,
        # and then add those nodes to the other new tree we are creating in the same manner
        # Maybe we can do this recursively?
        if not root:
            return root

        copy = TreeNode(root.val,self._swap(root.right) if root.right else None,self._swap(root.left) if root.left else None)
        return copy
    def _swap(self,root):
        if root == None:
            return None
        return TreeNode(root.val,self._swap(root.right) if root.right else None,self._swap(root.left) if root.left else None)
