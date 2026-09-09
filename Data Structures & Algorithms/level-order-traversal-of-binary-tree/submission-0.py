# Definition for a binary tree node.
"""
We have a tree, and we are given its root. Our job is to return a list containing sublists with the values of the nodes at each level of the tree. What data structure should we use for this problem? It will be a BFS problem. What do you use for BFS? I think I would use a queue. We start at the root. We add that first, then we add its children to a queue. At each iteration, we add the children node to a new sublist that was created, and we also add its children to the queue. [1,2,3,4,5,6,7] -> [[1]]. We are returning a list of integers by the way, not the actual nodes themselves. How do we use a queue for this? we want to append to the left of the list 

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        my_deque = deque([root])
        while my_deque:
            sublist = []
            size = len(my_deque)
            count = 0
            while count < size:
                node = my_deque.pop()
                sublist.append(node.val)
                if node.left:
                    my_deque.appendleft(node.left)
                if node.right:
                    my_deque.appendleft(node.right)
                count+=1
            out.append(sublist)
        return out

                

        