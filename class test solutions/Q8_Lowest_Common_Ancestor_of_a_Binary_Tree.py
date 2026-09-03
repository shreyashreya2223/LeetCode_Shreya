# Q8. Lowest Common Ancestor of a Binary Tree
# Time: O(n) | Space: O(h) recursion stack
#
# Uses the standard LeetCode TreeNode definition.

def lowestCommonAncestor(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right
