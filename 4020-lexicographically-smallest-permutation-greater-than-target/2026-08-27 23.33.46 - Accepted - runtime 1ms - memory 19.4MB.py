class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            cur = ord(target[i]) - ord('a')

            # If we can match target[i], do it
            if cnt[cur] > 0:
                ans.append(target[i])
                cnt[cur] -= 1
                continue

            # Cannot match target[i].
            # First, try making THIS position greater.
            for c in range(cur + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Remaining characters in sorted order
                    for k in range(26):
                        ans.extend([chr(k + ord('a'))] * cnt[k])

                    return ''.join(ans)

            # Cannot make current position greater.
            # Backtrack to an earlier position.
            for j in range(i - 1, -1, -1):
                # Restore the character at position j
                old = ord(ans.pop()) - ord('a')
                cnt[old] += 1

                cur = ord(target[j]) - ord('a')

                # Try the smallest character > target[j]
                for c in range(cur + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Fill suffix minimally
                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * cnt[k])

                        return ''.join(ans)

            return ""

        # We matched target exactly.
        # Need the next lexicographically greater permutation.
        for i in range(len(target) - 1, -1, -1):
            old = ord(ans.pop()) - ord('a')
            cnt[old] += 1

            cur = ord(target[i]) - ord('a')

            for c in range(cur + 1, 26):
                if cnt[c] > 0:
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    for k in range(26):
                        ans.extend([chr(k + ord('a'))] * cnt[k])

                    return ''.join(ans)

        return ""