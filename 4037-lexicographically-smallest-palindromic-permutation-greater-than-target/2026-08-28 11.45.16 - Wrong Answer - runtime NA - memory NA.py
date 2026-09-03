class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # A palindrome can have at most one odd count
        odd = [i for i in range(26) if cnt[i] % 2]
        if len(odd) > 1:
            return ""

        # Characters available in the left half
        half = [c // 2 for c in cnt]

        # Middle character
        mid = chr(odd[0] + 97) if odd else ""

        m = n // 2
        target_half = target[:m]

        def build(left):
            left_str = ''.join(chr(i + 97) * left[i] for i in range(26))
            return left_str + mid + left_str[::-1]

        # ---------------------------------------------------------
        # Try to make the left half:
        #
        # target_half[0:i] + bigger_character + smallest_suffix
        #
        # We try i from right to left so that the resulting
        # permutation is the smallest possible one.
        # ---------------------------------------------------------

        for i in range(m - 1, -1, -1):

            remaining = half[:]
            prefix = []
            possible = True

            # Consume target_half[0:i]
            for j in range(i):
                c = ord(target_half[j]) - 97

                # IMPORTANT:
                # Actually consume the character.
                if remaining[c] == 0:
                    possible = False
                    break

                remaining[c] -= 1
                prefix.append(c)

            if not possible:
                continue

            # At position i, choose the smallest character
            # strictly greater than target_half[i].
            cur = ord(target_half[i]) - 97

            bigger = -1
            for c in range(cur + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            remaining[bigger] -= 1

            # Fill the rest with the smallest possible characters
            suffix = []
            for c in range(26):
                suffix.extend([c] * remaining[c])

            left = prefix + [bigger] + suffix

            # Sanity: left must have exactly m characters
            if len(left) != m:
                continue

            ans = build_from_list(left, mid, n)

            if ans > target:
                return ans

        # ---------------------------------------------------------
        # Also check if target's first half itself is possible.
        # The resulting palindrome may be > target because of
        # the second half.
        # ---------------------------------------------------------

        remaining = half[:]
        left = []

        for ch in target_half:
            c = ord(ch) - 97

            if remaining[c] == 0:
                return ""

            remaining[c] -= 1
            left.append(c)

        ans = build_from_list(left, mid, n)

        if ans > target:
            return ans

        return ""


def build_from_list(left, mid, n):
    left_str = ''.join(chr(c + 97) for c in left)

    if n % 2:
        return left_str + mid + left_str[::-1]

    return left_str + left_str[::-1]