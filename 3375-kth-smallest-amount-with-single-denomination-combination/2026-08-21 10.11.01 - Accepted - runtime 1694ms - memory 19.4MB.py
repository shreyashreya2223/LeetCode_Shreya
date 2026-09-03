from math import gcd

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """
            Count distinct amounts <= x
            that are divisible by at least one coin.
            """
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        # No multiples <= x
                        if current_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // current_lcm
                else:
                    total -= x // current_lcm

            return total

        # The answer cannot be larger than k * smallest coin
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left