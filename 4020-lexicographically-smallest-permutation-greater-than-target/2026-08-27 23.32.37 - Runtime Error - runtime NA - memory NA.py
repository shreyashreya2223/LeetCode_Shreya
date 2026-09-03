class Solution:
    def lexSmallestPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                ans.append(target[i])
                cnt[x] -= 1
            else:
                # Backtrack
                for j in range(i - 1, -1, -1):
                    c = ord(ans.pop()) - ord('a')
                    cnt[c] += 1

                    cur = ord(target[j]) - ord('a')

                    # Find smallest character > target[j]
                    for k in range(cur + 1, 26):
                        if cnt[k] > 0:
                            ans.append(chr(k + ord('a')))
                            cnt[k] -= 1

                            # Add remaining characters in sorted order
                            for x in range(26):
                                ans.extend([chr(x + ord('a'))] * cnt[x])

                            return ''.join(ans)

                return ""

        # target itself is possible.
        # Find next greater permutation.
        for i in range(len(target) - 1, -1, -1):
            c = ord(ans.pop()) - ord('a')
            cnt[c] += 1

            cur = ord(target[i]) - ord('a')

            for k in range(cur + 1, 26):
                if cnt[k] > 0:
                    ans.append(chr(k + ord('a')))
                    cnt[k] -= 1

                    for x in range(26):
                        ans.extend([chr(x + ord('a'))] * cnt[x])

                    return ''.join(ans)

        return ""