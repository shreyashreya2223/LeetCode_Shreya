class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # More than one odd count => impossible palindrome
        odd = [i for i in range(26) if cnt[i] & 1]
        if len(odd) > 1:
            return ""

        mid = chr(odd[0] + 97) if odd else ""

        # Counts available for the left half
        half = [x // 2 for x in cnt]
        m = n // 2

        # ---------------------------------------------------------
        # Build palindrome from a left-half string
        # ---------------------------------------------------------
        def make_pal(left):
            if n % 2:
                return left + mid + left[::-1]
            return left + left[::-1]

        # ---------------------------------------------------------
        # We construct the left half.
        #
        # Case 1:
        # At some position i, left[i] > target[i].
        #
        # Then everything after i should be as small as possible.
        #
        # Case 2:
        # The entire left half equals target[:m].
        # Then we must compare the COMPLETE palindrome with target.
        # ---------------------------------------------------------

        # First try exact target prefix.
        remaining = half[:]
        left = []
        possible = True

        for i in range(m):
            c = ord(target[i]) - 97

            if remaining[c] == 0:
                possible = False
                break

            remaining[c] -= 1
            left.append(chr(c + 97))

        if possible:
            candidate = make_pal(''.join(left))

            if candidate > target:
                return candidate

        # ---------------------------------------------------------
        # Try making the left half larger at position i.
        #
        # We go from right -> left.
        # This gives the smallest possible number greater than target.
        # ---------------------------------------------------------

        for i in range(m - 1, -1, -1):

            remaining = half[:]

            # Match target[0:i]
            ok = True

            for j in range(i):
                c = ord(target[j]) - 97

                if remaining[c] == 0:
                    ok = False
                    break

                remaining[c] -= 1

            if not ok:
                continue

            # At position i, choose the smallest character
            # strictly greater than target[i].
            cur = ord(target[i]) - 97

            bigger = -1

            for c in range(cur + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            remaining[bigger] -= 1

            # Prefix is exactly target[:i]
            prefix = target[:i]

            # Fill the remaining positions minimally
            suffix = []

            for c in range(26):
                suffix.append(chr(c + 97) * remaining[c])

            left = prefix + chr(bigger + 97) + ''.join(suffix)

            candidate = make_pal(left)

            if candidate > target:
                return candidate

        return ""