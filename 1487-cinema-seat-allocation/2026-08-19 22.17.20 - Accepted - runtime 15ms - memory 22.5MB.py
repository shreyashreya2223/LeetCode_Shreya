class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats using a bitmask
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0
            rows[row] |= (1 << (seat - 1))

        # Rows with no reservations can always fit 2 groups
        ans = (n - len(rows)) * 2

        # Seat blocks:
        # Left   = 2,3,4,5
        # Middle = 4,5,6,7
        # Right  = 6,7,8,9

        left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)
        middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6)
        right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)

        for mask in rows.values():
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            if can_left and can_right:
                ans += 2
            elif can_left or can_middle or can_right:
                ans += 1

        return ans