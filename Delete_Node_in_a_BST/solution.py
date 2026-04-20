class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        if key == root.val:
            if root.left and root.right:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                root = root.right
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
