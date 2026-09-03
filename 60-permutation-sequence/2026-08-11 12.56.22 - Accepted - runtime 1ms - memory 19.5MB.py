import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1, n + 1)))
        k -= 1
        ans = ""

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            ans += nums.pop(idx)
            k %= fact

        return ans