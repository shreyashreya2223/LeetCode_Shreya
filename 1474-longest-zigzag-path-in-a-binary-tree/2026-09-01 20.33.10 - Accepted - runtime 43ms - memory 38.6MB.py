class Solution:
    def longestZigZag(self, root):
        self.ans = 0

        def dfs(node, left, right):
            if not node:
                return

            # If we go left, the next move must be right
            if node.left:
                dfs(node.left, 0, left + 1)
            else:
                dfs(node.left, 0, 0)

            # If we go right, the next move must be left
            if node.right:
                dfs(node.right, right + 1, 0)
            else:
                dfs(node.right, 0, 0)

            self.ans = max(self.ans, left, right)

        dfs(root, 0, 0)

        return self.ans