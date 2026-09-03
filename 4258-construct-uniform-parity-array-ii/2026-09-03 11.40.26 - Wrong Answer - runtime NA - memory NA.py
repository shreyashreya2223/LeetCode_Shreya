class Solution:
    def check(self, nums, target):
        # min_val[0] = smallest even number seen so far
        # min_val[1] = smallest odd number seen so far
        min_val = [float('inf'), float('inf')]

        for x in nums:
            parity = x % 2

            # Option 1: keep x as it is
            if parity == target:
                min_val[parity] = min(min_val[parity], x)
                continue

            # Option 2: x - y
            # We need y such that:
            # (x - y) % 2 == target
            needed = parity ^ target

            # y must be smaller than x
            if min_val[needed] >= x:
                return False

            # x can be used by future elements
            min_val[parity] = min(min_val[parity], x)

        return True

    def uniformArray(self, nums1):
        # Try making everything even OR everything odd
        return self.check(nums1, 0) or self.check(nums1, 1)