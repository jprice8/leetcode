import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 


class Solution:
    def isValidBst(self, root: TreeNode) -> bool:
        # set up stack for inorder DFS
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True


if __name__ == '__main__':
    # instantiate root node
    root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))

    s = Solution()
    print(s.isValidBst(root))