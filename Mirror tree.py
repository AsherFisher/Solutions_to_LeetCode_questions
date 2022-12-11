# Definition for a binary tree node.
import math

import self as self


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.root = None
        self.arr = []

    def isSymmetric(self, root):

        if root is None:
            return True
        
        i = 0
        self.root = root
        self.printTree(self.root)
        print(self.arr)
        size = len(self.arr)

        while i != int(size/2):
            if self.arr[i] != self.arr[size - i - 1]:
                return False
            i += 1

        return True

    def printTree(self, root):
        if not root:
            return

        self.printTree(root.left)
        self.arr.append(root.val)
        self.printTree(root.right)


if __name__ == "__main__":
    i = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
                 TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))

    b = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(4, TreeNode(5, None, None), None))


    s = Solution()
    print(s.isSymmetric(b))
