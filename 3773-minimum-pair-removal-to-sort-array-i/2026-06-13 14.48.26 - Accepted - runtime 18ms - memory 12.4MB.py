class Solution:
    def minimumPairRemoval(self, nums):
        nums = nums[:]
        ops = 0
        while True:
            # check if non-decreasing
            if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
                return ops
            # find leftmost pair with minimum sum
            min_sum = float('inf')
            idx = 0
            for i in range(len(nums)-1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    idx = i
            nums[idx:idx+2] = [min_sum]
            ops += 1