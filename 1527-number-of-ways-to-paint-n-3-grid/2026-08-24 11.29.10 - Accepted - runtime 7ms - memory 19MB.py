class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        a = 6  # 3 different colors
        b = 6  # 2 colors

        for _ in range(1, n):
            new_a = (2 * a + 2 * b) % MOD
            new_b = (2 * a + 3 * b) % MOD

            a = new_a
            b = new_b

        return (a + b) % MOD