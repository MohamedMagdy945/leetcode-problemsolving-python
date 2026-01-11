class Solution:
    def __init__(self):
        self.st = set()
    def _Traversal(self ,node: Optional[TreeNode]):
        if not node :
            return 
        self.st.add(node.val)
        self._Traversal(node.left)
        self._Traversal(node.right)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self._Traversal(root)
        self.st = sorted(self.st)
        i = 1
        minDiff = 989898999
        while i < len(self.st):
            if self.st[i] != self.st[i - 1]:
                minDiff = min(minDiff , self.st[i] - self.st[i - 1])
            i += 1
        return minDiff