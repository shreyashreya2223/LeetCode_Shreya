class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, rem):
            if not rem:
                res.append(path)
                return
            for i in range(len(rem)):
                backtrack(path + [rem[i]], rem[:i] + rem[i+1:])

        backtrack([], nums)
        return res