from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])

        max_sum = float('-inf')
        answer = 1
        level = 1

        while queue:
            level_size = len(queue)
            current_sum = 0

            for _ in range(level_size):
                node = queue.popleft()

                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Update only if strictly greater
            if current_sum > max_sum:
                max_sum = current_sum
                answer = level

            level += 1

        return answer