class Solution:
    def check(self, nums, target):
        min_val = [float('inf'), float('inf')]

        # Find global minimum even and odd
        for x in nums:
            min_val[x % 2] = min(min_val[x % 2], x)

        for x in nums:
            parity = x % 2

            # Already has the required parity
            if parity == target:
                continue

            # Need to subtract a number of opposite parity
            needed = parity ^ target

            # There must be a strictly smaller number
            if min_val[needed] >= x:
                return False

        return True

    def uniformArray(self, nums1):
        # Try making everything even or everything odd
        return self.check(nums1, 0) or self.check(nums1, 1)