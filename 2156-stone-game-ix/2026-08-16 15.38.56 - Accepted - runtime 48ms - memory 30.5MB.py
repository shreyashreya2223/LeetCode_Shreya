class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        # If there are no remainder-1 or remainder-2 stones,
        # Alice cannot avoid losing.
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        # If cnt[0] is even, Alice wins if both types exist.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # If cnt[0] is odd, Alice needs one type to have
        # at least two more stones than the other.
        return abs(cnt[1] - cnt[2]) > 2