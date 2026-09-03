class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find the complete swappable group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Values in this group are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Get their original positions
            indices = [arr[i][1] for i in range(start, end + 1)]
            indices.sort()

            # Put smallest values at smallest indices
            for i in range(len(values)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans