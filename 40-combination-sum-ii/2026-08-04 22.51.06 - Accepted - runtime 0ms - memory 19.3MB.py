class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                ans.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no need to continue
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # i+1 because each element can be used only once
                backtrack(i + 1, path, remaining - candidates[i])

                path.pop()

        backtrack(0, [], target)
        return ans