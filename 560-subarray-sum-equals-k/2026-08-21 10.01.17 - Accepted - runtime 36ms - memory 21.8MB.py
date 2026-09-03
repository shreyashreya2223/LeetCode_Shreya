class Solution:
    def subarraySum(self, nums, k):
        freq = {0: 1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            # Check if there is a previous prefix sum
            # such that the subarray between them sums to k
            if prefix - k in freq:
                count += freq[prefix - k]

            # Store the current prefix sum
            freq[prefix] = freq.get(prefix, 0) + 1

        return count