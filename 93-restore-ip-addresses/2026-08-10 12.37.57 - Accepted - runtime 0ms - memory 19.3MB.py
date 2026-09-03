class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []

        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    ans.append(".".join(parts))
                return

            for j in range(i + 1, min(i + 4, len(s) + 1)):
                x = s[i:j]

                if (x[0] == '0' and len(x) > 1) or int(x) > 255:
                    continue

                backtrack(j, parts + [x])

        backtrack(0, [])
        return ans