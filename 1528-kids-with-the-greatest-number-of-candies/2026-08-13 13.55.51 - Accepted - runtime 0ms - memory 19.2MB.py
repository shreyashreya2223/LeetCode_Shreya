class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        return [c + extraCandies >= mx for c in candies]