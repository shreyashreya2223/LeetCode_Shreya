class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        # If current node is p or q
        if root == p or root == q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q are in different subtrees
        if left and right:
            return root

        # Otherwise, return whichever side found a node
        if left:
            return left

        return right