class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if current node is good
            good = 1 if node.val >= max_val else 0
            
            # Update maximum value on this path
            max_val = max(max_val, node.val)
            
            # Count good nodes in both subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        return dfs(root, root.val)