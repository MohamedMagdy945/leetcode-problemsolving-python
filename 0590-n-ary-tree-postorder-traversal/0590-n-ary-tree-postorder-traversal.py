"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.postorderList = []
    def Traversal(self,root:Optional['Node']):
        if not root :
            return

        for i in root.children or []:
            self.Traversal(i)
        self.postorderList.append(root.val)

    def postorder(self,root:'Node') -> List[int]:
        self.Traversal(root)
        return self.postorderList
