from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()

        n = len(senate)

        # Store the indices of each party
        for i, ch in enumerate(senate):
            if ch == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            # The senator with the smaller index acts first
            if r < d:
                # R bans D
                R.append(r + n)
            else:
                # D bans R
                D.append(d + n)

        return "Radiant" if R else "Dire"