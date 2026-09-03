class Solution:
    def longestSubsequence(self, nums):

        total_xor = 0
        has_non_zero = False

        for num in nums:
            total_xor ^= num

            if num != 0:
                has_non_zero = True

        # All elements are zero
        if not has_non_zero:
            return 0

        # XOR of all elements is already non-zero
        if total_xor != 0:
            return len(nums)

        # Remove one non-zero element
        return len(nums) - 1