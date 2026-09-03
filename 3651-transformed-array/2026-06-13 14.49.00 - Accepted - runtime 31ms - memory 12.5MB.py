class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = []
        for i, v in enumerate(nums):
            if v == 0:
                result.append(0)
            else:
                result.append(nums[(i + v) % n])
        return result