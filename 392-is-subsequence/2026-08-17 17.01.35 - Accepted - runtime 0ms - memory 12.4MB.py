class Solution:
    def isSubsequence(self, s, t):
        j = 0

        for char in t:
            if j < len(s) and s[j] == char:
                j += 1

        return j == len(s)