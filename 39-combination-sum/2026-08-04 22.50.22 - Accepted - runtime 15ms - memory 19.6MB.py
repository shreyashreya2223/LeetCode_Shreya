class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(index, curr, total):
            if total == target:
                ans.append(curr[:])
                return

            if index == len(candidates) or total > target:
                return

            # Include current candidate
            curr.append(candidates[index])
            backtrack(index, curr, total + candidates[index])

            # Backtrack
            curr.pop()

            # Exclude current candidate
            backtrack(index + 1, curr, total)

        backtrack(0, [], 0)
        return ans