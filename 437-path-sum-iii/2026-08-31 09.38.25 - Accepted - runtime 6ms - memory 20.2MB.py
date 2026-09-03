class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix = {0: 1}
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            current_sum += node.val
            
            # Number of paths ending at current node
            # whose sum is targetSum
            count = prefix.get(current_sum - targetSum, 0)
            
            # Add current prefix sum
            prefix[current_sum] = prefix.get(current_sum, 0) + 1
            
            # Explore children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Remove current prefix sum when going back
            prefix[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)